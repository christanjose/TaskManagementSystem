from django.shortcuts import render, redirect
from django.contrib import messages
from tasksapp.models import TaskDb
from projectsapp.models import ProjectDb
from accountsapp.models import CustomUser


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
        due_date = request.POST.get("due_date")

        project = ProjectDb.objects.get(id=project_id)
        member = CustomUser.objects.get(id=assigned_to)

        task = TaskDb(Task_Title=task_title, Task_Description=task_description,
            Project=project, Assigned_To=member, Due_Date=due_date
        )

        task.save()
        messages.success(request, "Task created successfully!")
        return redirect("list_project")