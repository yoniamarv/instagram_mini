from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pics', blank=True)
    follows = models.ManyToManyField(
        'Profile', related_name='followed_by', symmetrical=False, blank=True)

    def __str__(self):
        return (self.user.username) + ' ' + str(self.id)


class Post(models.Model):
    picture = models.ImageField(upload_to='post_pics', blank=True)
    description = models.TextField()
    date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
