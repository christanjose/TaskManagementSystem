from django.urls import path
from projectsapp import views


urlpatterns = [
    path('create_project/', views.create_project, name='create_project'),
    path('save_project/', views.save_project, name='save_project'),
    path('list_project/', views.list_project, name='list_project'),
    path('delete_project/<int:pro_id>', views.delete_project, name='delete_project'),
    path('edit_project/<int:pro_id>', views.edit_project, name='edit_project'),
    path('update_project/<int:pro_id>', views.update_project, name='update_project'),
]