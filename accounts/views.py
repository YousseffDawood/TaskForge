from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from accounts.models import User
from project.models import Project, Task, Comment
from django.db.models import Q
from accounts.models import User  # adjust if needed

def home(request):
    """
    Renders the home dashboard for the authenticated user.
    Displays active projects, open tasks, completed tasks, and total employee count.
    """
    user=request.user

    user_projects = Project.objects.filter(Q(project_owner=user) | Q(project_members=user)).distinct()
    open_tasks = Task.objects.filter(project__in=user_projects, status__in=['TODO', 'IN_PROGRESS'])
    completed_tasks = Task.objects.filter(project__in=user_projects, status='DONE')

    total_members = User.objects.filter(roles='EMPLOYEE').count()

    context = {
        'active_projects_count': user_projects.count(),
        'open_tasks_count': open_tasks.count(),
        'completed_tasks_count': completed_tasks.count(),
        'total_members_count': total_members,
    }

    return render(request, 'home.html', context)

def login_view(request):
    """
    Handles user login.
    Authenticates user credentials and redirects to the home page on success.
    """
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        elif user is None:
            return render(request, 'login.html', {'error': "Invalid username or password."})
    elif request.method == 'GET':
        return render(request, 'login.html')  

def signup_view(request):
    """
    Handles new user registration.
    Validates input, assigns appropriate roles based on job title, and creates a new User object.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        email = request.POST.get('email')
        job_title= request.POST.get('job_titles')
        if job_title == 'CLIENT':
            Role = User.Roles.Customer
        else:
            Role = User.Roles.Employee
        
        # if job_title := request.POST.get('job_title'):
        #     Role=User.Roles.Employee
        # else:
        #     job_title=None
        #     Role=User.Roles.Customer


        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('sign_up')

        if User.objects.filter(username=username).exists():
            return render(request, 'sign_up.html', {'error': "Username already exists"})

        if User.objects.filter(email=email).exists():
            return render(request, 'sign_up.html', {'error': "Email already exists"})

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            job_title=job_title,
            roles=Role
        )

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'sign_up.html', {'job_titles': User.job_titles.choices})
def logout_view(request):
    """
    Logs out the current user and redirects to the login page.
    """
    logout(request)
    return redirect('login')

# def Notifications(request):
#     return render(request, 'notifications.html')