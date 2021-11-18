
from django.urls import path
from . import views

# app_name in urls.py is the name spacing and you'll have to add a colon APP_NAME: before route in views.py redirect and in template url
app_name = "todo"

urlpatterns = [
    path('tasks/', views.index , name='index'),
    # this seems like a better way to create at tasks/add instead of tasks/. but i don't know for sure 
    path('tasks/add/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.tasks, name='view_task'),
    path('tasks/<int:task_id>/update/', views.update_task, name='update_task'),
    # path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    # why did i do this to myself again
]