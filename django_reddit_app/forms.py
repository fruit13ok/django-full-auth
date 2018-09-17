from django import forms
from django_reddit_app.models import UserProfileInfo, Post, Comment
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'picture', 'content', 'site_url', 'vote_total', 'user')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'vote_total', 'user', 'post')