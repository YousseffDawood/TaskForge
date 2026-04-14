from django.urls import path, include
from . import views
urlpatterns = [
    path('projects/', views.projects_detail, name='projects_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('create_project/', views.create_project, name='create_project'),
    path('add_member/<int:project_id>/', views.add_member, name='add_member'),
    path('create_task/', views.create_task, name='create_task'),
    path('task/<int:task_id>/', views.view_task, name='task_detail'),
    path('tasks/', views.tasks_list, name='task_list'),
    path('add_comment/<int:task_id>/', views.add_comment, name='add_comment'),
    path('update_task/<int:task_id>/', views.update_task_status, name='update_task_status'),
    path('projects/<int:project_id>/update_status/', views.update_project_statuses, name='update_project_status'),
    path('admin/', views.admin_panel, name='admin_panel'),
    path('admin/users/', views.promote_users, name='promote_users'),
    path('admin/user/<int:user_id>/role/', views.change_user_role, name='change_user_role'),
    path('admin/project/<int:project_id>/members/', views.admin_manage_member, name='admin_manage_member'),
    path('notifications/', views.notifications, name='notifications'),
]
