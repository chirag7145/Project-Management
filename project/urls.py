from django.urls import path, include
from .views import *


urlpatterns = [
    path('users/', AllUsers, name='allUsers'),
    path('users/<str:username>', GetUser, name='getUser'),
    path('projects/', AllProjects, name='allProjects'),
    path('projects/<str:title>', GetProject, name='getProject'),
]
