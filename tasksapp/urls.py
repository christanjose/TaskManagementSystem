from django.urls import path
from tasksapp import views
from tasksapp.views import my_tasks

urlpatterns = [
    path('create_task/<int:pro_id>/', views.create_task, name="create_task"),
    path('save_task/', views.save_task, name="save_task"),
    path('list_task/', views.list_task, name="list_task"),
    path('project_task/<int:pro_id>/', views.project_task, name="project_task"),
    path('delete_task/<int:task_id>/', views.delete_task, name="delete_task"),
    path('edit_task/<int:task_id>/', views.edit_task, name="edit_task"),
    path('update_task/<int:task_id>/', views.update_task, name="update_task"),

    path('my_tasks/', views.my_tasks, name="my_tasks"),
    path('task_detail/<int:task_id>/', views.task_detail, name="task_detail"),
    path('save_comment/<int:task_id>/', views.save_comment, name="save_comment"),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name="edit_comment"),
    path('update_comment/<int:comment_id>/', views.update_comment, name="update_comment"),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name="delete_comment"),

]