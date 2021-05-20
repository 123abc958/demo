# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
# from __future__ import unicode_literals
from .models import Profile, Post
from django.shortcuts import render
from django.db.models import Q
from .forms import PostAddForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
   profile = Profile.objects.all().order_by('-id')
   post=Post.objects.all().order_by('-id')
   return render(request, 'demo_app/index.html', {'profile': profile, 'post': post,})
  
 
def about(request):
   return render(request, 'demo_app/about.html')

def post(request): 
   return render( request, 'demo_app/post.html', {'post':post})

def detail(request, post_id):
   post = get_object_or_404(Post, id=post_id)
   return render(request, 'demo_app/detail.html', {'post': post})

def access(request):
   return render(request, 'demo_app/access.html')

def add(request):
   if request.method == "POST":
      form = PostAddForm(request.POST, request.FILES)
      if form.is_valid():
         post = form.save(commit=False)
         post.user = request.user
         post.save()
         return redirect('demo_app:index')
   else:   
       form = PostAddForm()
   return render(request, 'demo_app/add.html', {'form': form})

def edit(request, post_id):
   post = get_object_or_404(Post, id=post_id)
   if request.method == "POST":
       form = PostAddForm(request.POST, request.FILES, instance=post)
       if form.is_valid():
           form.save()
           return redirect('demo_app:detail', post_id=post.id)
   else:
       form = PostAddForm(instance=post)
   return render(request, 'demo_app/edit.html', {'form': form, 'post':post })

def delete(request, post_id):
   post = get_object_or_404(Post, id=post_id)
   post.delete()
   return redirect('demo_app:index')





