from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now


class List(models.Model): 

    title = models.CharField("List Name", max_length=250, unique=True) 

    def __str__(self): 

        return self.title


class Item(models.Model): 

  title = models.CharField("Item Name", max_length=250) 

  created_date = models.DateTimeField(default=datetime.datetime.now) 

  todo_list = models.ForeignKey(List)

  def __str__(self): 

    return self.title 

