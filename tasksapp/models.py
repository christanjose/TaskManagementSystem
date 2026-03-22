from django.db import models
from projectsapp.models import ProjectDb
from accountsapp.models import CustomUser

class TaskDb(models.Model):
    Task_Title = models.CharField(max_length=200)
    Task_Description = models.TextField()
    Project = models.ForeignKey(ProjectDb, on_delete=models.CASCADE, related_name="tasks")
    Assigned_To = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="assigned_tasks")

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]

    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    Priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    Due_Date = models.DateField()
    Created_At = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['Due_Date']
        unique_together = ('Project', 'Task_Title')

    def __str__(self):
        return self.Task_Title


class TaskCommentDb(models.Model):
    Task = models.ForeignKey(TaskDb, on_delete=models.CASCADE, related_name="comments")
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Comment = models.TextField()
    Created_AT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Comment