from re import template
from django.shortcuts import render

# Create your views here.
def BlogHome(request):
    template_name = "blog.html"
    return render(request, template_name)

def IndexPage(request):
    template_name = 'index.html'
    return render(request, template_name)