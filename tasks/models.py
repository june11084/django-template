from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Task: " + self.task + ", Created: " + str(self.created_at)


class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name
