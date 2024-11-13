from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from kafka import KafkaProducer, KafkaConsumer
import json

# Create your views here.

@login_required(login_url='/login/')
def home_page(request):

    if request.method == "POST":
     data=request.POST
     task_name=data.get('enter_task')
     print(task_name)

     #Send the input/received data to Kafka Server
     producer = KafkaProducer(bootstrap_servers="localhost:29092")
     producer.send("task details", json.dumps(data).encode("utf-8")) #'task_details' is a Kafka Topic Name
     print(f"Done Sending..")

     #Create the Task object and store details in Database.

     Tasks.objects.create(
        task_name=task_name,
        task_completed=False,
      #   user=User.objects
        user=User.objects.get(id=request.user.id),
        profile=Profile.objects.get(user=request.user.id)
        
     )
     return redirect("/home/")
    
    consumer = KafkaConsumer('task_details', bootstrap_servers='localhost:29092') #Retrieves Task details from Kafka Server. 'task_details' is a Kafka topic from where,we retrieve or store data.
    kafka_server_data=json.loads(consumer)

    all_tasks=Tasks.objects.filter(user=request.user.id)  #user=request.user.id bhako user ko task haru matrai dekhauni where (request.user.id) gives the id of currently logged in user
   #  context1={'all_tasks': all_tasks}

   #  context2={'first_task': all_tasks[0]}           #for displaying name in the home page(i.e. base model), passing another context by referencing to only one task(so that we get object instead of list and so that we don't have to use loop in the home page(base.html) to display user's name and image). Basically, this is just to identify the user through a task.

    context={'all_tasks': all_tasks, 'first_task': all_tasks.first(), 'kafka_server_tasks': kafka_server_data}
    return render(request, 'home.html', context)

# #Class view for the Home page

# class Home_Page(ListView):
#    model=Tasks
#    context_object_name='all_tasks'
#    template_name='home.html'

# class Create_Page(CreateView):
#    model=Tasks
#    context_object_name='all_tasks'
#    fields='__all__'
#    template_name='home.html'
#    success_url='home.html'   

def check_box(request, task_name):
   selected_task=Tasks.objects.get(task_name=task_name)
   if selected_task.task_completed==False:
      selected_task.task_completed=True
      selected_task.save()
      return redirect("/home/")

   if selected_task.task_completed==True:
      selected_task.task_completed=False
      selected_task.save()
      return redirect("/home/")

   # print("working")
   # return redirect("/home/")

def reset_all_tasks(request):
   # print("working")
   all_tasks=Tasks.objects.filter(user=request.user.id)
   # print(all_tasks)
   for task in all_tasks:
      # print (task.task_name)
      # task.task_completed= False  
      if task.task_completed==True:
         # print(task.task_name)
         task.task_completed=False
         task.save()

   
        
   return redirect("/home/")

def delete_all_tasks(request):

   all_tasks=Tasks.objects.filter(user=request.user.id)
   all_tasks.delete()

   return redirect("/home/")

def delete_task(request, task_name):
   task=Tasks.objects.get(task_name=task_name)
   task.delete()
   return redirect("/home/")


def update_task(request, task_name):
   task=Tasks.objects.get(task_name=task_name)   #filter returns set of objects and requires loop but get returns object so doesnot require loop, can be iterated directly
   if request.method == "POST":
      new_task_name=request.POST.get("task_name")
      print(new_task_name)
      print(task)

      task.task_name=new_task_name
      task.save()

      return redirect("/home/")
   
   context={'selected_task': task}

   return render(request, "update_task.html", context)

# #Class view for Update Task

# class Update_Task(UpdateView):
#    model=Tasks
#    context_object_name='selected_task'
#    template_name='update_task.html'
   
