from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
  # this one-to-one relationship allows us to 'extend' our user
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  portfolio_site = models.URLField(blank=True)
  profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

  def __str__(self):
    return self.user.username
