from django.shortcuts import get_object_or_404, render_to_response, redirect, get_list_or_404
from todo.models import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from random import randint
from todo.forms import *
import datetime

@login_required(login_url='/login/')
def home(request):
    return render_to_response('todo/home.html',{},RequestContext(request))
@login_required(login_url='/login/')
def tower(request):
    p = get_object_or_404(Tower,user=request.user.username)
    monstertype =randint(1,8)
    level = p.level
    exptolevelup = (level*0.5)*100
    cleanexp = '%g'%(exptolevelup)
    if request.method == 'POST':
        if p.ap > 0:
            p.ap -= 1
            p.save()
        else:
            p.ap = 0
            p.save()
        if p.trigger != 0:
            p.trigger = 0
            p.save()
        
        
        
        rvalue = randint(1,100)
        monsterchance = randint(1,100)
        goldamt = randint(20,100)
        if 1 <= rvalue <= 10:
            p.state = 1
            p.money += 50+(level*randint(1,5))
            p.save()
        elif 11 <= rvalue <= 70:
            p.state = 2
            p.steps += 1;
            if p.steps == 25:
                p.steps = 0
                p.towerlevel += 1
                p.exp += 10+(level*0.6)
                if p.exp >= exptolevelup:
                    p.level += 1
                    p.exp = 0
                    p.trigger = 3
                p.trigger = 2
            p.save()
        else:
            p.state = 3
            
            if monsterchance <= 30:
                p.hp -= 10
                p.exp += randint(5,10)+(level*0.6)
                p.save()
            else:
                p.exp += randint(5,10)
                if p.exp >= exptolevelup:
                    p.level += 1
                    p.exp = 0
                    p.trigger = 3
                p.save()
            if p.hp <= 0:
                p.trigger = 1
                p.hp = 100
                p.save()
    else:
        p.state = 0
        p.trigger = 0
        p.save()
    return render_to_response('todo/tower.html',{'tower':p,'type':monstertype,'expreq':cleanexp},RequestContext(request))
@login_required(login_url='/login/')
def shop(request):
    
    def moneycheck(money,item):
        if item == 'potion':
            if money >= 75:
                p.money -= 75
                p.hp += 10
                return True
            else:
                return False
        if item == 'map':
            if money >= 100:
                p.money -= 100
                p.steps += 1
                if p.steps == 25:
                    p.steps = 0
                    p.towerlevel += 1
                    p.exp += 10+(level*0.6)
                    if p.exp >= exptolevelup:
                        p.level += 1
                        p.exp = 0
                        p.trigger = 3
                    p.trigger = 2
                return True
            else:
                return False
        if item == 'potion2':
            if money >= 200:
                p.money -= 200
                p.exp += 10*p.level
                if p.exp >= exptolevelup:
                    p.level += 1
                    p.exp = 0
                    p.trigger = 3
                return True
            else:
                return False
    p = get_object_or_404(Tower,user=request.user.username)
    level = p.level
    exptolevelup = float((level*0.5)*100)
    cleanexp = '%g'%(exptolevelup)
    confirm = 0
    item = 0
    money = p.money
    if request.method == 'POST':
        if 'potion' in request.POST:
            if moneycheck(money,'potion'):
                confirm = 2
                item = 'Health Potion'
            else:
                confirm = 1
        if 'map' in request.POST:
            if moneycheck(money,'map'):
                confirm = 2
                item = 'Map'
            else:
                confirm = 1
        if 'potion2' in request.POST:
            if moneycheck(money,'potion2'):
                confirm = 2
                item = 'Experience Potion'
            else:
                confirm = 1
    p.save()
    return render_to_response('todo/shop.html',{'tower':p,'confirm':confirm,'item':item,'expreq':cleanexp},RequestContext(request))


#Registration code from http://www.djangobook.com/en/2.0/chapter14.html
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            p = Tower(ap=0,state=0,hp=100,money=0,exp=0,level=1,towerlevel=1,steps=0,trigger=0,user=request.POST['username'])
            p.save()
            
            
            #----------------------------group---
	    gm = GroupMember(g_member = request.POST['username'])
            gm.save()
            #----------------------------group---
            
         
            new_user = form.save()
            new_user = authenticate(username=request.POST['username'],password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect("/home/")
    else:
        form = UserCreationForm()
    return render(request, "todo/register.html", {
        'form': form,
    })

#http://hily.me/blog/2008/11/learning-django-ch6/
@login_required(login_url='/login/')
def addtask(request):
        doing = 0
        for t in Task.objects.filter(user = request.user.username).order_by('-time'):
		#if (t.exp_time - datetime.datetime.now()).days  < -1:
		if timediff(t.exp_time,datetime.datetime.now()):
			t.expired = True
			t.save()
			p = get_object_or_404(Tower,user=request.user.username)
			p.ap -= 1
			p.save()
        if request.method == 'POST': 
                form = addtaskForm(request.POST) 
                if form.is_valid():
                	task = form.cleaned_data['task']
                	user = request.user.username
                	exp_time = datetime.datetime(int(form.cleaned_data['exp_year']), int(form.cleaned_data['exp_month']), 
                		int(form.cleaned_data['exp_day']),int(form.cleaned_data['exp_hour']),int(form.cleaned_data['exp_min']))
                	if timediff(exp_time,datetime.datetime.now()):
                                doing = 4
                		form = addtaskForm()
                                tasks = Task.objects.filter(user = request.user.username).order_by('-time')
                                return render(request,'todo/task.html', {
                                    'form': form,'tasks':tasks,'state':doing
                        })     
                	t = Task(task = task,user = user,exp_time = exp_time)
                	t.save()
                	doing = 1
                        form = addtaskForm()
                        tasks = Task.objects.filter(user = request.user.username).order_by('-time')
                        return render(request,'todo/task.html', {
                            'form': form,'tasks':tasks,'state':doing
                        })   
        else:
            doing = 0
            form = addtaskForm()
        tasks = Task.objects.filter(user = request.user.username).order_by('-time')
        return render(request,'todo/task.html', {
                'form': form,'tasks':tasks,'state':doing
        })   
@login_required(login_url='/login/')
def deletetask(request,id):
	task = get_object_or_404(Task,pk = int(id))
	gid = task.group_id
	task.delete()
	doing = 2
	if gid != -1:
		return checkgroup(request,gid)
        form = addtaskForm()
        tasks = Task.objects.filter(user = request.user.username).order_by('-time')
        return render(request,'todo/task.html', {
                'form': form,'tasks':tasks,'state':doing
        })   

def deletetaskComp(request,id):
	task = get_object_or_404(Task,pk = int(id))
	task.delete()
	doing = 2
        tasks = Task.objects.filter(user = request.user.username).order_by('-time')
        return render(request,'todo/completed.html', {
                'tasks':tasks,'state':doing
        })
def deletetaskExp(request,id):
	task = get_object_or_404(Task,pk = int(id))
	task.delete()
	doing = 2
        tasks = Task.objects.filter(user = request.user.username).order_by('-time')
        return render(request,'todo/expired.html', {
                'tasks':tasks,'state':doing
        }) 
def completetask(request,id):
	task = get_object_or_404(Task,pk = int(id))
	task_id = int(id)
	print task.group_id
	if task.group_id != -1:
		if task.accept == 1:
                        p = get_object_or_404(Tower,user=task.assignto)
                        p.ap += randint(1,3)
                        p.save()
			task.complete = True
			task.com_time = datetime.datetime.now()
			task.save()
			return checkgroup(request,task.group_id)
		return completegrouptask(request,task_id)
	task.complete = True
	task.com_time = datetime.datetime.now()
	task.save()
	doing = 3
        p = get_object_or_404(Tower,user=request.user.username)
        p.ap += randint(1,3)
        p.save()
	form = addtaskForm()
        tasks = Task.objects.filter(user = request.user.username).order_by('-time')
        return render(request,'todo/task.html', {
                'form': form,'tasks':tasks,'state':doing
        })   
def completed(request):
    doing = 0
    tasks = Task.objects.filter(user = request.user.username).order_by('-time')
    return render(request,'todo/completed.html', {
                'tasks':tasks,'state':doing
    }) 
def expired(request):
    doing = 0
    tasks = Task.objects.filter(user = request.user.username).order_by('-time')
    return render(request,'todo/expired.html', {
                'tasks':tasks,'state':doing
    })

#===============================================================================
#=========new Group part========================================================
def group(request):
	req = 0
	errdate = 0
        try:
        	#groups = []
        	#for i in range(0, len(GroupMember.objects.filter(g_member = request.user.username)):
        	gm = GroupMember.objects.get(g_member = request.user.username)
        	#groups.add(gm.group_set.all())
		groups = gm.group_set.all()  	
		
        except GroupMember.DoesNotExist:
        	groups = None
        if request.method == 'POST' and request.POST['action'] == "Create Group": 
                aform = addgroupForm(request.POST)
                jform = joingroupForm()
                iform = inviteuserForm()
                if aform.is_valid():
                    errdate = 4
                    name = aform.cleaned_data['g_name']
                    leader = request.user.username
                    gm = GroupMember.objects.get(g_member = leader)
                    g = Group(g_name = name,g_leader = leader)
                    g.save()
                    
                else:
                    errdate = 3
                    groups = Group.objects.all()
                    return render(request,'todo/grouplist.html',{'gmember':None,'aform':aform,'groups':groups,'errdate':errdate})
		g.members.add(gm)
        
	else:
		tform = None
        	aform = addgroupForm()
        	jform = joingroupForm()
        	iform = None
	return render(request,'todo/group.html', {
			'gmember':None,'errdate':errdate,
	'aform': aform,'iform': iform,'jform': jform,'groups':groups,'tasks':None,'tform': None})
	
@login_required(login_url='/login/')
def checkgroup(request,id):
	errdate = 0
	req = 0
	try:
        	#groups = []
        	#for i in range(0, len(GroupMember.objects.filter(g_member = request.user.username)):
        	gm = GroupMember.objects.get(g_member = request.user.username)
        		#groups.add(gm.group_set.all())
		groups = gm.group_set.all()
		
        except GroupMember.DoesNotExist:
        	groups = None
        for t in Task.objects.filter(group_id=int(id)).order_by('-time'):
		if timediff(t.exp_time,datetime.datetime.now()):
			t.expired = True
			t.save()
			p = get_object_or_404(Tower,user=request.user.username)
			if p.ap > 0:
                            p.ap -= 1
                            p.save()
	if request.method == 'POST' and request.POST['action'] == "Invite User":
		iform = inviteuserForm(request.POST)
                if iform.is_valid():
                        req = 2
                	u = iform.cleaned_data['user']
                	try:
                		gm = GroupMember.objects.get(g_member = u)
                		g = Group.objects.get(id = int(id))
                		inviter = request.user.username
                		invite(inviter,int(id),u)
                	except Group.DoesNotExist:
                		g = None
                	except GroupMember.DoesNotExist:
                		gm = None
        elif request.method == 'POST' and request.POST['action'] == "Add Task":
        	form = addtaskForm(request.POST) 
                if form.is_valid():
                        req = 1
                	task = form.cleaned_data['task']
                	assignto = form.cleaned_data['assignto']
                	group_id = int(id)
                	group = get_object_or_404(Group,pk = int(id))
                	gm = group.members.all()
                	for x in gm:
                		if x.g_member == assignto:
                			errdate = 0
                			break
                		else: 
                			errdate = 2
                			
                	exp_time = datetime.datetime(int(form.cleaned_data['exp_year']), int(form.cleaned_data['exp_month']), 
                		int(form.cleaned_data['exp_day']),int(form.cleaned_data['exp_hour']),int(form.cleaned_data['exp_min']))
			if timediff(exp_time,datetime.datetime.now())==False and errdate == 0:
                                #doing = 4        
                                t = Task(task = task,group_id = group_id,exp_time = exp_time,assignto = assignto)
                                t.save()
                        else:
                            if errdate != 2:
                        	errdate = 1
        else:
        	None
        group = get_object_or_404(Group,pk = int(id))
        if group.g_leader == request.user.username:
        	tform = addtaskForm()
        else:
        	tform = None
        aform = addgroupForm()
        jform = joingroupForm()
        iform = inviteuserForm()
        tasks = Task.objects.filter(group_id = int(id)).order_by('-time')
        gmember = group.members.all()
        return render(request,'todo/group.html', {
        		'gmember':gmember,'iform': iform,
        		'aform': aform,'jform': jform,'groups':groups,
        		'tasks':tasks,'tform': tform,'group':group,'errdate':errdate,'req':req
        })


def message(request):
	nouserfound = 0
	try:
        	message = Message.objects.filter(owner = request.user.username)      	
        except Message.DoesNotExist:
        	message = None
        if request.method == 'POST' and request.POST['action'] == "Send Message":
            
        	form = sendmessageForm(request.POST) 
                if form.is_valid():
                	content = form.cleaned_data['message']
                	owner = form.cleaned_data['sendto']
                	if not User.objects.filter(username=owner).exists():
                		nouserfound = 1
                	else:
                                nouserfound = 2
                		m = Message(sender = request.user.username,content = content,owner = owner)
                		m.save()
        mform = sendmessageForm()
	return render(request,'todo/message.html', {
			"message":message,"mform":mform,"nouserfound":nouserfound
	})
def acceptinvite(request,id):
	group = get_object_or_404(Group,pk = int(id))
	gm = GroupMember.objects.get(g_member = request.user.username)
        group.members.add(gm)
        Message.objects.filter(group = int(id)).delete()
	return message(request)
	
def invite(inviter,gid,sendtouser):
	owner = sendtouser
	g = Group.objects.get(id = int(gid))
	content = inviter + " want you to join group of: " + g.g_name
	m = Message(sender = inviter,group = gid, content = content,owner = owner)
	m.save()
def completegrouptask(request, task_id):
	t = Task.objects.get(id = int(task_id))
	gid = t.group_id
	group = Group.objects.get(id = int(gid))
	leader = group.g_leader
	gname = group.g_name
	content = "Group: "+gname + " Task: "+ t.task + " claimed by " + t.assignto +" as complete"
	m = Message(sender = t.assignto,task = task_id, content = content,owner = leader,group = gid)
	m.save()
	return checkgroup(request, gid)
def accepttaskcomplete(request,id):
	
	t = get_object_or_404(Task,pk = int(id))
	t.accept = 1
	t.save()
        Message.objects.filter(task = int(id)).delete()
        
	return completetask(request,id)
def quitgroup(request,id):
	group1 = get_object_or_404(Group,pk = int(id))
	Task.objects.filter(group_id = int(id),assignto =request.user.username).delete()
	gm = GroupMember.objects.get(g_member = request.user.username)
	group1.members.remove(gm)
	leader = group1.g_leader
	sender = request.user.username
	gname = group1.g_name
	content = "User: "+sender + " has left your group: " +gname
	m = Message(sender = sender, content = content,owner = leader)
	m.save()
	if leader == sender:
		group1.delete()
	return group(request)
def delmessage(request,id):
	m = get_object_or_404(Message,pk = int(id))
	m.delete()
	return message(request)
def grouplist(request):
    aform = addgroupForm()
    groups = Group.objects.all()
    return render(request,'todo/grouplist.html', {"groups":groups,"aform":aform})
def joingroup(request,id):
	gm = GroupMember.objects.get(g_member = request.user.username)
	g = Group.objects.get(id = int(id))
	g.members.add(gm)
	group1 = get_object_or_404(Group,pk = int(id))
	leader = group1.g_leader
	sender = request.user.username
	gname = group1.g_name
	content = "User: "+sender + " has joined your group: " +gname
	m = Message(sender = sender, content = content,owner = leader)
	m.save()
	return grouplist(request)
def kickmember(request,gid,mid):
	g = get_object_or_404(Group,pk = int(gid))
	gm = get_object_or_404(GroupMember,pk = int(mid))
	if g.g_leader == request.user.username:
		Task.objects.filter(group_id = int(gid),assignto = gm.g_member).delete()
		g.members.remove(gm)
		sender = request.user.username
		gname = g.g_name
		owner = gm.g_member
		content = "You has been kick from group: "+gname
		m = Message(sender = sender, content = content,owner = owner)
		m.save()
	return checkgroup(request,gid)
def timediff(t1,t2):
	diff = (t1-t2).days
	#t1<t2
	if diff<-1:
		return True
	#if on the same day
	elif diff == -1:
		t1_s = t1.hour*3600 + t1.minute*60
		t2_s = t2.hour*3600 + t2.minute*60
		if (t1_s - t2_s)<0:
			return True
	return False
