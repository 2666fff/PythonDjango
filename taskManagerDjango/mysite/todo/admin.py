from todo.models import *
from django.contrib import admin



admin.site.register(Task)
admin.site.register(Tower)

#=============================
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Message)
