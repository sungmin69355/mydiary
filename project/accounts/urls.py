from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout_request, name='logout'),
    path('change_password_page/',views.change_password_page, name ='change_password_page')
]
