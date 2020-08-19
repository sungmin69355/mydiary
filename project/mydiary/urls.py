from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('write_diary',views.write_diary,name='write_diary'),
    path('view_diary',views.view_diary,name='view_diary'),
    path('create',views.create,name='create'),
    path('mypage', views.mypage,name='mypage'),
    path('detail/<int:posts_id>/',views.detail,name='detail'), 
    path('delete/<int:posts_id>/',views.delete,name='delete'),
    path('update/<int:posts_id>/',views.update,name='update'),#여기 수정중... html에서 값을 post 값을 넘긴다음 그 넘긴 값으로 업로드를해줘야함
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)