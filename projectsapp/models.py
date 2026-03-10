from django.db import models
from accountsapp.models import CustomUser

class ProjectDb(models.Model):
    Project_Name = models.CharField(max_length=200, unique=True)
    Project_Description = models.TextField()
    Start_Date = models.DateField()
    End_Date = models.DateField()
    Project_Owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="owned_projects")
    Project_Members = models.ManyToManyField(CustomUser, related_name="member_projects")
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Project_Name
