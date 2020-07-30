from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photo = models.ImageField(null=True,blank=True)
    content = models.CharField(max_length=4000)
    pub_date = models.DateTimeField(auto_now=True)
    weather = models.CharField(max_length=15)
    emotion = models.CharField(max_length=15)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()
        
    def __str__(self):
        return "%s - %s" % (self.username, self.title)