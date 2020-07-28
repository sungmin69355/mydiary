from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    nick_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.nick_name)