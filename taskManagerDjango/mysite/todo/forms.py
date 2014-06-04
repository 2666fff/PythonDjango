#changed models.py task.html urls.py forms.py admin.py

from django import forms
from datetime import datetime

now = datetime.now()
class addtaskForm(forms.Form):
    task = forms.CharField(required=True,label = "New Task Name")
    exp_year = forms.ChoiceField(choices=[(x, x) for x in range(now.year, now.year+6)],label = 'Due year:')
    exp_month = forms.ChoiceField(choices=[(x, x) for x in range(1, 13)],label = 'Due month:')    
    exp_day = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)],label = 'Due day:')
    exp_hour = forms.ChoiceField(choices=[(x, x) for x in range(1, 24)],label = 'Due hour:')
    exp_min = forms.ChoiceField(choices=[(x, x) for x in [0,15,30,45]],label = 'Due minut:')
    assignto = forms.CharField(required=False,label = "Assign to group member(username):")
#=========new Group part===========
class addgroupForm(forms.Form):
	g_name = forms.CharField(required=True,label = "New Group Name")

class joingroupForm(forms.Form):
	g_id = forms.IntegerField(required=True,label = "Join Group ID")
	
class inviteuserForm(forms.Form):
	user = forms.CharField(required=True,label = "Invite User Name:")
	#g_id = forms.IntegerField(required=True,label = "Invite to Group ID:")
class sendmessageForm(forms.Form):
	sendto = forms.CharField(required=True,label = "Send To Username:")
	message = forms.CharField(required=True,label = "Message content:",widget=forms.Textarea)
	
