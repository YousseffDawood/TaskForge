from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    class status(models.TextChoices):
        TODO = "TODO", "To Do"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        DONE = "DONE", "Done"
    state=models.CharField(max_length=20,choices=status.choices,default=status.TODO)
    project = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    project_owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='owned_projects')
    project_members = models.ManyToManyField('accounts.User', related_name='projects')

    def __str__(self):
        return self.project_name


class Task(models.Model):
    task=models.AutoField(primary_key=True)
    task_name=models.CharField(max_length=255)
    task_description=models.TextField()
    assigned_to=models.ForeignKey('accounts.User',on_delete=models.CASCADE,related_name='assigned_tasks')
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='tasks')
    assigner=models.ForeignKey('accounts.User',on_delete=models.CASCADE,related_name='assigner')
    status=models.CharField(max_length=20,choices=Project.status.choices,default=Project.status.TODO)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task_name
class Comment(models.Model):
    comment=models.AutoField(primary_key=True)
    comment_text=models.TextField()
    commented_by=models.ForeignKey('accounts.User',on_delete=models.CASCADE,related_name='comments')
    task=models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    def __str__(self):
        return self.comment_text[:20]  
class Notification(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message[:30]}"