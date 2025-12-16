from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True) 
    important = models.BooleanField(default=False)
    completed = models.BooleanField(default=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    document = models.FileField(upload_to='task_documents/', blank=True, null=True)

    def __str__(self):
        return self.title + '- by ' + self.user.username
    class Meta:
        ordering = ['-created']
    def mark_complete(self):
        self.completed = True
        self.datecompleted = timezone.now()
        self.save()