from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #photo = models.ImageField()
    content = models.CharField(max_length=4000)
    published = models.DateTimeField(auto_now=True)
    weather = models.CharField(max_length=15)
    emotion = models.CharField(max_length=15)

    def __str__(self):
        return "%s - %s" % (self.username, self.title)