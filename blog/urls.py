from django.urls import path
from blog import views

urlpatterns = [
    path(r'', views.posts, name='posts'),
]