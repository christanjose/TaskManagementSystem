from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accountsapp.models import CustomUser
from projectsapp.models import ProjectDb
from tasksapp.models import TaskDb
from django.contrib import messages

def login_page(request):
    return render(request, "login.html")

def login_view(request):

    if request.method == "POST":
        uname = request.POST.get("username")
        pswd = request.POST.get("password")

        user = authenticate(request, username=uname, password=pswd)

        if user is not None:
            login(request, user)
            return redirect(dashboard)
        else:
            messages.error(request, "Invalid username or password")
            return redirect(login_page)
    return redirect(login_page)

def logout_view(request):
    logout(request)
    return redirect(login_page)

def create_member(request):
    return render(request, "create_member.html")

def save_member(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        CustomUser.objects.create_user(username=username, email=email, password=password,
                role="member"
        )
        return redirect(list_member)
    return redirect(create_member)

def list_member(request):
    members = CustomUser.objects.filter(role="member")
    return render(request, "list_member.html", {'members':members})

def delete_member(request, memb_id):
    member = CustomUser.objects.get(id=memb_id)
    member.delete()
    return redirect(list_member)

@login_required
def dashboard(request):

    if request.user.role == "admin":

        project_count = ProjectDb.objects.count()
        user_count = CustomUser.objects.filter(role="member").count()
        task_count = TaskDb.objects.count()
        completed_tasks = TaskDb.objects.filter(Status="completed").count()

        return render(request, "dashboard.html", {
            'project_count': project_count,
            'user_count': user_count,
            'task_count': task_count,
            'completed_tasks': completed_tasks,
        })

    else:

        my_task_count = TaskDb.objects.filter(Assigned_To=request.user).count()
        pending_count = TaskDb.objects.filter(Assigned_To=request.user, Status="pending").count()
        in_progress_count = TaskDb.objects.filter(Assigned_To=request.user, Status="in_progress").count()
        completed_tasks = TaskDb.objects.filter(Assigned_To=request.user, Status="completed").count()

        return render(request, "dashboard.html", {
            'my_task_count': my_task_count,
            'pending_count': pending_count,
            'in_progress_count': in_progress_count,
            'completed_tasks': completed_tasks,
        })