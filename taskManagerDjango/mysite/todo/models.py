from django.db import models

class Tower(models.Model):
    ap = models.IntegerField()
    state = models.IntegerField()
    hp = models.IntegerField()
    money = models.IntegerField()
    exp = models.IntegerField()
    level = models.IntegerField()
    towerlevel = models.IntegerField()
    steps = models.IntegerField()
    trigger = models.IntegerField()
    user = models.CharField(max_length=500)
    def __unicode__(self):
	return '%s' % (self.user)
class Task(models.Model):
    task = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=500)
    complete = models.BooleanField(default=0)
    exp_time = models.DateTimeField('Due Date')
    com_time = models.DateTimeField(auto_now_add=True)
    expired =  models.BooleanField(default=0)
    group_id = models.IntegerField(default = -1)
    assignto = models.CharField(max_length=500)
    accept = models.IntegerField(default = -1)
    def __unicode__(self):
	return '%s: %s' % (self.user, self.task)
   
#=========new Group part===========	
class GroupMember(models.Model):
	g_member = models.CharField(max_length=500)
	def __unicode__(self):  
		return self.g_member  
	class Meta:  
		db_table = "gm" 
class Group(models.Model):
	g_leader = models.CharField(max_length=500)
	g_name = models.CharField(max_length = 50)
	members = models.ManyToManyField(GroupMember)
	def __unicode__(self):
		return '%s: %s' % (self.g_name, self.g_leader)
	class Meta:  
		db_table = "group" 
#=========new Group part===========end

#=========new Group part===========	
class Message(models.Model):
	owner = models.CharField(max_length=500)
	sender = models.CharField(max_length=500)
	content = models.CharField(max_length=500)
	send_time = models.DateTimeField(auto_now_add=True)
	group = models.IntegerField(default = -1)
	task = models.IntegerField(default = -1)
	class Meta:  
		db_table = "message" 

