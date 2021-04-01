# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Profile, Post
from django.shortcuts import render

# Create your views here.
def index(request):
  profile = Profile.objects.get(id=1)
  return render(request, 'demo_app/index.html', {'profile': profile})
 
def about(request):
   return render(request, 'demo_app/about.html')

def post(request):
   post=Post.objects.all().order_by('-id')
   return render( request, 'demo_app/post.html', {'post':post})

