from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class List(models.Model): 
    title = models.CharField("", max_length=250, unique=False, editable=True) 
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.title


class Item(models.Model): 
  title = models.CharField("", max_length=250, unique=False) 
  created_date = models.DateTimeField(default=datetime.datetime.now) 
  todo_list = models.ForeignKey(List, on_delete=models.CASCADE)

  def __str__(self): 
    return self.title 
