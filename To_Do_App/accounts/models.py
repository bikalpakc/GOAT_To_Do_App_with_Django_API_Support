from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(BaseModel):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image=models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)        
