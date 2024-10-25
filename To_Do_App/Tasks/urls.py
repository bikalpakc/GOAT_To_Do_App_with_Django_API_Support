from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name="home_page"),
    # path('home/', Home_Page.as_view(), name="home_page"), #format for Class based views
    path('', home_page, name="home_page"), 
    # path('', Home_Page.as_view(), name="home_page"), #format for Class based views
    path('home/check-box/<task_name>/', check_box, name="check_box"),
    path('home/reset/', reset_all_tasks, name="reset_all_tasks"),
    path('home/delete-all/', delete_all_tasks, name="delete_all_tasks"),
    path('home/delete-task/<task_name>', delete_task, name="delete_task"),
    path('home/update-task/<task_name>', update_task, name="update_task"),
    # path('home/update-task/<task_name>', Update_Task.as_view(), name="update_task"), #format for Class based views
    path('api/', include('Tasks.api.urls')),  #path to Tasks API.
]
