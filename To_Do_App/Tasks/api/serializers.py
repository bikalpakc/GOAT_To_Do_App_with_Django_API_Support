from Tasks.models import Tasks
from rest_framework import serializers

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tasks
        fields=['profile', 'user', 'task_name', 'task_completed']
        lookup_field = 'task_name' #To change detail slug in routers url to 'task_name' instead of 'id'.
