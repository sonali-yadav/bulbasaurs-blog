from django.shortcuts import render, get_object_or_404
from blog.models import Post


def posts(request):
    posts_list = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts': posts_list})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def error_404(request, exception):
    return render(request, 'blog/page_not_found.html', {})
