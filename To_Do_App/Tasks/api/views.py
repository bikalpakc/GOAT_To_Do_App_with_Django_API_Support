from Tasks.models import Tasks
from Tasks.api.serializers import TasksSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class TasksViewSet(viewsets.ModelViewSet):
    queryset=Tasks.objects.all()
    serializer_class=TasksSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    lookup_field = 'task_name'  #To change detail slug in routers url to 'task_name' instead of 'id'.

    #To display data of only logged in User, not of other users.
    def get_queryset(self):
        user=self.request.user
        return Tasks.objects.filter(user=user)