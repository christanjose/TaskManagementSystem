from django.shortcuts import render, redirect
from django.contrib import messages
from projectsapp.models import ProjectDb
from accountsapp.models import CustomUser


def create_project(request):
    members = CustomUser.objects.filter(role="member")
    return render(request, "create_project.html", {"members": members})


def save_project(request):

    if request.method == "POST":
        project_name = request.POST.get("project_name")
        project_description = request.POST.get("project_description")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        project = ProjectDb(Project_Name=project_name, Project_Description=project_description, Start_Date=start_date,
            End_Date=end_date, Project_Owner=request.user
        )

        project.save()
        members = request.POST.getlist("project_members")
        project.Project_Members.set(members)
        messages.success(request, "Project created successfully!")
        return redirect(create_project)

def list_project(request):
    projects = ProjectDb.objects.all()
    return render(request, "list_project.html", {"projects": projects})

def delete_project(request, pro_id):
    project = ProjectDb.objects.get(id=pro_id)
    project.delete()
    return redirect(list_project)

def edit_project(request, pro_id):
    data = ProjectDb.objects.get(id=pro_id)
    members = CustomUser.objects.filter(role="member")
    return render(request, "edit_project.html", {
        'data':data,
        'members':members
    })

def update_project(request, pro_id):

    if request.method == "POST":

        project_name = request.POST.get('project_name')
        project_description = request.POST.get('project_description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        ProjectDb.objects.filter(id=pro_id).update(Project_Name=project_name, Project_Description=project_description,
            Start_Date=start_date, End_Date=end_date
        )

        project = ProjectDb.objects.get(id=pro_id)
        members = request.POST.getlist("project_members")
        project.Project_Members.set(members)
        return redirect(list_project)