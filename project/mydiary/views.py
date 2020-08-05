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
    #post.photo = request.FILES['image']
    posts.content = request.POST['text']
    posts.weather = request.POST['radio_weather']
    posts.emotion = request.POST['radio_emotion']
    posts.save()
    posts = Post.objects.all().order_by('-id')
    return render(request, 'view_diary.html',{'posts':posts})
    
def detail(request,posts_id):
    post_detail = get_object_or_404(Post, pk=posts_id)
    return render(request, 'detail_view.html', {'post_detail':post_detail})

def delete(request, posts_id):
    post = Post.objects.get(id=posts_id)
    post.delete()
    posts = Post.objects.all().order_by('-id')
    return render(request, 'view_diary.html',{'posts':posts})