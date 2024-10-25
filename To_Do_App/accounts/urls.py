from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('logout/', logout_page, name="logout_page"),
    path('add-profile-picture/', add_profile_picture, name="add_profile_picture"),
    path('accounts/', include('allauth.urls')),
]
