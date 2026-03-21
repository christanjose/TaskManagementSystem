from django.shortcuts import render, redirect
from django.contrib import messages
from projectsapp.models import ProjectDb
from tasksapp.models import TaskDb
from django.contrib.auth.decorators import login_required
from datetime import datetime


# _______________ Admin Views _______________

def create_task(request, pro_id):

    project = ProjectDb.objects.get(id=pro_id)
    members = project.Project_Members.all()

    return render(request, "create_task.html", {
        "project": project,
        "members": members
    })

def save_task(request):

    if request.method == "POST":

        task_title = request.POST.get("task_title")
        task_description = request.POST.get("task_description")
        project_id = request.POST.get("project_id")
        assigned_to = request.POST.get("assigned_to")
        priority = request.POST.get("priority")
        due_date = request.POST.get("due_date")

        task = TaskDb(Task_Title=task_title, Task_Description=task_description,
            Project_id=project_id, Assigned_To_id=assigned_to, Priority=priority, Due_Date=due_date
        )

        task.save()
        messages.success(request, "Task created successfully!")
        return redirect(project_task, pro_id=project_id)

def list_task(request):
    tasks = TaskDb.objects.all()
    today = datetime.now().date()
    return render(request, "list_task.html", {
        'tasks':tasks,
        'today':today
    })

def project_task(request, pro_id):
    project = ProjectDb.objects.get(id=pro_id)
    project_tasks = TaskDb.objects.filter(Project_id=pro_id)
    today = datetime.now().date()
    return render(request, "project_task.html", {
        'project':project,
        'project_tasks':project_tasks,
        'today':today
    })

def delete_task(request, task_id):
    task = TaskDb.objects.get(id=task_id)
    task.delete()
    return redirect(list_task)

def edit_task(request, task_id):
    data = TaskDb.objects.get(id=task_id)
    project = data.Project
    members = project.Project_Members.all()
    return render(request, "edit_task.html", {
        'data': data,
        'members': members
    })

def update_task(request, task_id):

    if request.method == "POST":

        task_title = request.POST.get('task_title')
        task_description = request.POST.get('task_description')
        assigned_to = request.POST.get('assigned_to')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')

        TaskDb.objects.filter(id=task_id).update(Task_Title=task_title,Task_Description=task_description,
            Assigned_To_id=assigned_to, Priority=priority, Status=status, Due_Date=due_date)
        return redirect(list_task)


# _______________ Admin Views _______________

@login_required
def my_tasks(request):

    if request.method == "POST":
        task_id = request.POST.get("task_id")
        status = request.POST.get("status")
        TaskDb.objects.filter(id=task_id, Assigned_To=request.user).update(Status=status)
        return redirect(my_tasks)

    tasks = TaskDb.objects.filter(Assigned_To=request.user)
    today = datetime.now().date()

    return render(request, "my_tasks.html", {
        "tasks": tasks,
        "today": today
    })