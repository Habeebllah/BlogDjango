from .models import *

def blog_renderer(request):
    cate = Category.objects.all()
    category = Category.objects.all()
    counts = []
    for c in cate:
        category_count = Blog.objects.filter(category=c).count()
        counts.append(category_count)
    print(counts)

    cat_count = zip(cate, counts) 
    side_recent_post = Blog.objects.all().order_by('-created_at')[8:11]
    side_popular_post = Blog.objects.all().order_by('-created_at')[12:16]

    return {
       'category': category,
       'cat_count': cat_count,
       'side_popular_post': side_popular_post,
       'side_recent_post': side_recent_post,
       'counts': counts
    }