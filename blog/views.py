from django.shortcuts import render
from blog.models import Post


def posts(request):
    posts_list = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts': posts_list})
