from django.db import models
from accounts.models import *
from base.models import BaseModel

# Create your models here.

class Tasks(BaseModel):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_name=models.CharField(max_length=50)
    # task_completed=models.CharField(max_length=50)
    task_completed=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.task_name
