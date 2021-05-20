from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'demo_app'
urlpatterns = [
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('post/', views.post, name='post'),
   path('detail/<int:post_id>/', views.detail, name='detail'),
   path('access/', views.access, name='access'),
   path('add/', views.add, name='add'),
   path('edit/<int:post_id>/', views.edit, name='edit'),
   path('delete/<int:post_id>/', views.delete, name='delete'), 
   
   # path('signup/', views.signup, name='signup'),

]