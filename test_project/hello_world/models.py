from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = timezone.now()
    models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Greeting(models.Model):
    title = models.CharField(max_length=50)

class Name(models.Model):
    title = models.CharField(max_length=100)
    models.ForeignKey(Greeting, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
