from django.urls import path, include
from Tasks.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('tasks', views.TasksViewSet, basename='tasks')

urlpatterns=[
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]