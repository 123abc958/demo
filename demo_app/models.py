# Create your models here.
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone 


class Profile(models.Model):
    name = models.CharField('名前', max_length=35)
    education = models.CharField('教育', max_length=35)
    github= models.CharField('GitHub', max_length=35)
    facebook= models.CharField('facebook', max_length=35)
    blog= models.CharField('blog', max_length=35)
    mail= models.CharField('mail', max_length=35)
    mobile = models.CharField('携帯', max_length=35)
    def __str__(self):
        return self.name

class Post(models.Model):
   title = models.CharField('タイトル', max_length=35)
   text = models.TextField('本文')
   created_at = models.DateTimeField('投稿日', default=timezone.now)   
   def __str__(self):
       return self.title
