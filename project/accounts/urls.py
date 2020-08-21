from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout_request, name='logout'),
    path('change_pw/',views.change_pw, name ='change_pw')
]
