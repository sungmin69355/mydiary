from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('write_diary',views.write_diary,name='write_diary'),
    path('view_diary',views.view_diary,name='view_diary'),
    path('create',views.create,name='create'),
    path('delete/<int:post_id>/',views.delete,name='delete'),    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)