from django.urls import path
from tasksapp import views

urlpatterns = [
    path('create_task/<int:pro_id>/', views.create_task, name="create_task"),
    path('save_task/', views.save_task, name="save_task"),
    path('list_task/', views.list_task, name="list_task"),
    path('project_task/<int:pro_id>/', views.project_task, name="project_task"),
    path('delete_task/<int:task_id>/', views.delete_task, name="delete_task"),
    path('edit_task/<int:task_id>/', views.edit_task, name="edit_task"),
    path('update_task/<int:task_id>/', views.update_task, name="update_task"),

]