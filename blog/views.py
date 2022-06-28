from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(requset, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(requset, 'blog/detail.html', {'blog':blog})

