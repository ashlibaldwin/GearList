
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, related_name='user')

    

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class List(models.Model): 

    title = models.CharField("", max_length=250, unique=False, editable=True) 
    user = models.ForeignKey(User, blank=True)
    def __str__(self): 

        return self.title


class Item(models.Model): 

  title = models.CharField("", max_length=250, unique=False) 
  #user = models.ForeignKey(UserProfile, null=False, default='admin')
  created_date = models.DateTimeField(default=datetime.datetime.now) 

  todo_list = models.ForeignKey(List)

  def __str__(self): 

    return self.title 

