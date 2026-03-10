from django.urls import path
from accountsapp import views

urlpatterns = [
    path('login_page/', views.login_page, name='login_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('create_member/', views.create_member, name='create_member'),
    path('save_member/', views.save_member, name='save_member'),
    path('list_member/', views.list_member, name='list_member'),
    path('delete_member/<int:memb_id>', views.delete_member, name='delete_member'),

]