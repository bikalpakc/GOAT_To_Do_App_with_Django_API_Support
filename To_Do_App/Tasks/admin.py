from django.contrib import admin
from .models import *
from accounts.models import *

# Register your models here.

# class TasksAdmin(admin.StackedInline):
#     model=Tasks

# class ProfileAdmin(admin.ModelAdmin):
#     # list_display=['product_name', 'price']
#     inlines=[TasksAdmin]  

# admin.site.register(Profile, ProfileAdmin)    


admin.site.register(Tasks)