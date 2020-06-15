from django.db import models

# Create your models here.
class Todo(models.Model):
    taskName=models.CharField(max_length=50)
    taskAssigned=models.DateField()
    taskDue=models.DateField()

def __str__(self):
    return self.taskName
