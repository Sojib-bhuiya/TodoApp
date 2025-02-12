from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('register/', views.user_register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('remaining_tasks/', views.remaining_tasks, name='remaining'),
    path('completed/', views.completedTask, name='completed'),
    path('delete/<int:task_id>', views.deleteTask, name='delete'),
    path('task_details/<int:task_id>', views.toggle_complete, name='task_detail'),
    path('toggle_complete/<int:task_id>', views.toggle_complete, name='toggle_complete'),
    path('remove_task/<int:task_id>', views.removeTask, name='remove_task'),
]
