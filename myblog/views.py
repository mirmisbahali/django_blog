from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from .models import Blog

# Create your views here.
def index(request):
    allBlogs = Blog.objects.all()
    context = {'allBlogs': allBlogs}
    return render(request, 'index.html', context)


def new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        date_created = datetime.now()
        b = Blog(title=title, desc=desc, date_created=date_created)
        b.save()
        return redirect('/blog')
    return render(request, 'new.html')