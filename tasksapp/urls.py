from django.urls import path
from tasksapp import views

urlpatterns = [
    path('create_task/<int:pro_id>/', views.create_task, name="create_task"),
    path('save_task/', views.save_task, name="save_task"),

]