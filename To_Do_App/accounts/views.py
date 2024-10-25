from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from requests import Response
from .models import *

# Create your views here.

def login_page(request):
    if request.method=="POST":
       username=request.POST.get('username')
       password=request.POST.get('password')
       print(username)

       if User.objects.filter(username=username).exists():
          user=authenticate(username=username, password=password)

          if user is None:
             messages.info(request, 'Invalid Password')
             redirect('/login/')

          else:
             login(request, user=user)
             profile=Profile.objects.get(user=request.user.id)
             print(profile.user.first_name)
             if (profile.profile_image):
               return redirect('/home/')
                          
             else:
                return redirect('/add-profile-picture/')
               

       else:
          messages.info(request, "Invalid Username")
          redirect("/login/")
                  



    return render(request, 'login.html')

def logout_page(request):
   logout(request)
   return redirect('/login/')

def register_page(request):

    if request.method == "POST":
     data=request.POST
     first_name=data.get('first-name')
     last_name=data.get('last-name')
     username=data.get('username')
     email=data.get('email')
     password=data.get('password')
   #   profile_image=request.FILES['profile_image']
    #  Or, profile_image=request.FILES.get('profile_image')

     user=User.objects.filter(username=username)
     if user.exists():
         messages.info(request, 'Username already taken')
         redirect("/register/")

     else:
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )

        user.set_password(password)

        user.save()
            
        messages.info(request, 'Account created successfully!')
        # time.sleep(10)
        return redirect("/register/")

    

    return render(request, 'register.html')


def add_profile_picture(request):
   if request.method == "POST":
      profile_picture=request.FILES.get('profile_picture')

      profile=Profile.objects.get(user=request.user.id)
      profile.profile_image=profile_picture
      profile.save()
      return redirect('/home/')

   return render(request, 'add_profile_picture.html')


