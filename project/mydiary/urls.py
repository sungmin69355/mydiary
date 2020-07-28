from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('write_diary',views.write_diary,name='write_diary'),
    path('view_diary',views.view_diary,name='view_diary'),
    path('create',views.create,name='create'),
]