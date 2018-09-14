# authly_app/urls.py
from django.urls import path
from authly_app import views

# SET THE NAMESPACE!
app_name = 'authly_app'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
]
