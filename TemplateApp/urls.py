from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'app'
URLPatterns = [
  path('home', views.home, name='home'),
  path('members', views.members, name='members'),
  path ('member/<int:id>', views.member, name='member')
]