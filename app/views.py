from django.shortcuts import render
from app.models import *

# Create your views here.
def BlogHome(request):
    template_name = "blog.html"
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, template_name, context)

def IndexPage(request):
    template_name = 'index.html'
    category = Category.objects.all()
    featured_post = Blog.objects.all()[:3]
    recent_post = Blog.objects.all().order_by('-created_at')[4:7]
    side_recent_post = Blog.objects.all().order_by('-created_at')[8:11]
    side_popular_post = Blog.objects.all().order_by('-created_at')[12:16]
    popular_post = Blog.objects.all().order_by('-created_at')[17]
    most_read_post = Blog.objects.all().order_by('-created_at')[18:22]
    context = {
        'category': category,
        'featured_post': featured_post,
        'recent_post': recent_post,
        'side_recent_post': side_recent_post,
        'popular_post': popular_post,
        'side_popular_post': side_popular_post,
        'most_read_post': most_read_post,
    }
    return render(request, template_name, context)