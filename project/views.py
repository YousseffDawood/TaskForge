from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Project, Task, Comment ,Notification
from django.db.models import Q
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from .decorator import role_required

@role_required(['CUSTOMER'])
def create_project(request):
    """
    Handles the creation of a new project.
    Only accessible by users with the 'CUSTOMER' role.
    """
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_description = request.POST.get('project_description')

        project = Project.objects.create(
            project_name=project_name,
            project_description=project_description,
            project_owner=request.user)

        if project:
            return redirect('projects_list')
        else:
            return render(request, 'project_create.html', {'error': 'Failed to create project.'})
    return render(request, 'project_create.html')
@role_required(['ADMIN'])
def add_member(request, project_id):
    """
    Adds a member to a specific project based on their username.
    Only accessible by users with the 'ADMIN' role.
    """
    if request.method == 'POST':
        project_id = request.POST.get('project_id', project_id)
        project = Project.objects.filter(project=project_id).first()
        member_username = request.POST.get('member_username')
        try:
            member = User.objects.get(username=member_username)
            project.project_members.add(member)
            return render(request, 'project_detail.html', {'project': project,'success': 'Member added successfully.'})
        except User.DoesNotExist:
            return render(request, 'project_detail.html', {'project': project,'error': 'User not found.'})
@role_required(['ADMIN','EMPLOYEE','CUSTOMER'])
def projects_detail(request):
    """
    Lists all projects accessible to the current user.
    Admins see all projects, while others see projects they own or are members of.
    """
    user = request.user
    if user.roles == 'ADMIN':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(Q(project_owner=user) | Q(project_members=user)).distinct()
    return render(request, 'project_list.html', {'projects': projects})
@role_required(['ADMIN','EMPLOYEE'])
def project_detail(request, project_id): 
    """
    Displays the details of a single project, including its tasks and comments.
    Accessible by ADMIN and EMPLOYEE roles.
    """
    try:
        project = Project.objects.get(project=project_id)
        return render(request, 'project_detail.html', {'project': project})
    except Project.DoesNotExist:
        return render(request, 'project_list.html', {'error': 'Project not found.'})
@role_required(['ADMIN'])
def create_task(request):
    """
    Handles the creation of a new task within a project.
    Sends a notification to the assigned employee upon creation.
    Only accessible by ADMIN role.
    """
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        project = Project.objects.filter(project=project_id).first()
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        assigner=request.user.id
        assigned_to_id=request.POST.get('assigned_to')
        try:
            project=Project.objects.get(project=project_id)
            task=Task.objects.create(
                task_name=task_name,
                task_description=task_description,
                project=project,
                assigner_id=assigner,
                assigned_to_id=assigned_to_id
            )
            Notification.objects.create(user=task.assigned_to,message=f"You have been assigned a new task '{task_name}' in project '{project.project_name}'.")
            return render(request, 'project_detail.html', {'project': project, 'success': 'Task created successfully.'})
        except Project.DoesNotExist:
            return redirect('projects_list')
    elif request.method == 'GET':
        members=User.objects.filter(roles='EMPLOYEE')
        return render(request, 'create_task.html', {'members': members})
@role_required(['ADMIN','EMPLOYEE'])
def tasks_list(request):
    """
    Lists all tasks that are assigned to or created by the current user.
    Accessible by ADMIN and EMPLOYEE roles.
    """
    user = request.user
    tasks = Task.objects.filter(Q(assigned_to=user) | Q(assigner=user)).distinct()
    return render(request, 'task_list.html', {'tasks': tasks})
@role_required(['ADMIN','EMPLOYEE'])
def view_task(request, task_id):
    """
    Displays the details of a specific task.
    Validates that the user is authorized to view it (assigner, assigned user, or admin).
    """
    # if request == 'POST':
        # if request.user.rolesin ['ADMIN','EMPLOYEE']:    
    user = request.user
    try:
        task = Task.objects.get(task=task_id)
        if user != task.assigned_to and user != task.assigner and user.roles != 'ADMIN':
            return render(request, 'task_detail.html', {'task': task, 'error': 'Not authorized.'})
        return render(request, 'task_detail.html', {'task': task})
    except Task.DoesNotExist:
        return redirect('task_list')
@role_required(['ADMIN','EMPLOYEE'])
def add_comment(request, task_id):
    """
    Adds a comment to a specific task.
    Accessible by ADMIN and EMPLOYEE roles.
    """
    if request.method == 'POST':
        comment_text =request.POST.get('comment_text')
        try:
            task=Task.objects.get(task=task_id)
            Comment.objects.create(
                comment_text=comment_text,
                commented_by=request.user,
                task=task)
            return render(request,'task_detail.html',{'task': task, 'success': 'Comment added successsfully'})
            
        except Task.DoesNotExist :
            return redirect('task_list')
@role_required(['ADMIN','EMPLOYEE'])
def update_task_status(request, task_id):
    """
    Updates the status of a specific task.
    Employees can only update tasks assigned to them.
    Notifications are sent when status is updated.
    """
    if request.method == 'POST':
        new_status = request.POST.get('status')
        try:
            task = Task.objects.get(task=task_id)
            if  request.user.roles == 'EMPLOYEE' and task.assigned_to != request.user:
                return render(request, 'task_detail.html', {'task': task, 'error': 'Only the assigned user can update the task status.'})
            task.status = new_status
            task.save()
            Notification.objects.create(user=task.assigned_to,message=f"Task '{task.task_name}' status updated to {new_status}.")
            return render(request, 'task_detail.html', {'task': task, 'success': 'Task status updated successfully.'})
        except Task.DoesNotExist:
            return redirect('task_list')
@role_required(['ADMIN'])                     
def update_project_statuses(request, project_id):
    """
    Updates the state/status of a specific project.
    Sends a notification to the project owner upon change.
    Only accessible by ADMIN role.
    """
    if request.method == 'POST':
        new_status = request.POST.get('state')
        try:
            project = Project.objects.get(project=project_id)
            project.state = new_status
            project.save()
            Notification.objects.create(user=project.project_owner,message=f"Your project '{project.project_name}' status changed to {new_status}.")
            return redirect('project_detail', project_id=project.project)
        except Project.DoesNotExist:
            return redirect('projects_list')
    return redirect('project_detail', project_id=project_id)
@role_required(['ADMIN'])                     
def admin_panel(request):
    """
    Renders the admin dashboard panel.
    Provides an overview of all users, projects, and employees.
    """
    all_users = User.objects.all().order_by('username')
    all_projects = Project.objects.all().prefetch_related('project_members')
    all_employees = User.objects.filter(roles='EMPLOYEE')
    return render(request, 'admin_panel.html', {
        'all_users': all_users,
        'all_Projects': all_projects,
        'all_employees': all_employees,
        'total_users': User.objects.count(),
    })
@role_required(['ADMIN'])                     
def promote_users(request):
    """
    Renders the page for promoting user roles.
    Only accessible by ADMIN role.
    """
    all_users = User.objects.all().order_by('username').prefetch_related('projects')
    return render(request, 'promote.html', {
        'all_users': all_users,
        'total_users': all_users.count()})
@role_required(['ADMIN'])                     
def change_user_role(request, user_id):
    """
    Changes the role of a specific user.
    Only accessible by ADMIN role.
    """
    
    return redirect('admin_panel')
@role_required(['ADMIN'])                     
def admin_manage_member(request, project_id):
    """
    Allows admins to add or remove members from a project from the admin panel.
    """
    if request.method == 'POST':
        action = request.POST.get('action')
        member_id = request.POST.get('member_id')
        project = get_object_or_404(Project, pk=project_id)
        member = get_object_or_404(User, pk=member_id)
        if action == 'add':
            project.project_members.add(member)
        elif action == 'remove':
            project.project_members.remove(member)
    return redirect('admin_panel')
@role_required(['ADMIN','CUSTOMER','EMPLOYEE'])
def notifications(request):
    """
    Displays notifications for the current user.
    Marks all unread notifications as read.
    """
    user_notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')
    user_notifications.filter(is_read=False).update(is_read=True)
    return render(request, 'notifications.html', {'notifications': user_notifications})
    