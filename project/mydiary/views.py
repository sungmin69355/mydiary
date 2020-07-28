from django.shortcuts import render ,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from accounts.models import User
from django.db import IntegrityError
import getpass
# Create your views here.

def home(request):
    return render(request,'home.html')

def write_diary(request):
    return render(request, 'write_diary.html')

@csrf_exempt
def view_diary(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'view_diary.html',{'posts':posts})

def create(request):
    posts = Post()
    posts.username = request.user
    posts.title = request.POST['title']
    posts.content = request.POST['text']
    posts.weather = request.POST['radio_weather']
    posts.emotion = request.POST['radio_emotion']
    posts.save()
    posts = Post.objects.all().order_by('-id')
    return render(request, 'view_diary.html',{'posts':posts})