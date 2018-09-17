from django.urls import path
from . import views
from django_reddit_project import settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  
    path('', views.index, name='index'),

    path('register', views.register, name='register'),
    path('user_login',views.user_login,name='user_login'),
    path('logout', views.user_logout, name='logout'),

    # path('api/users', views.sendJson, name='sendJson'),
    # path('special',views.special, name='special'),

    path('posts', views.post_list, name='post_list'),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('posts/new', views.post_create, name='post_create'),
    path('posts/<int:pk>/comments/new', views.comment_create, name='comment_create'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # look under django doc about imagefield, static means public, make those path public