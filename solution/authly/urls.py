from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from authly_app import views


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index, name='index'), 
    path('special', views.special, name='special'), 
    path('authly_app/', include('authly_app.urls')), 
    path('logout', views.user_logout, name='logout')
]
