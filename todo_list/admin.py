from django.contrib import admin
from .models import Task, AppInfo, Profile

admin.site.register(Task)
admin.site.register(AppInfo)
admin.site.register(Profile)