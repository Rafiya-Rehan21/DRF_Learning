# Create your models here.
# todo/models.py
from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, blank=True, related_name='liked_todos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
