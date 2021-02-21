from django.urls import path
from blog import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]