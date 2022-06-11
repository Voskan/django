from django.shortcuts import render
from .models import Post

def index(request):
  news = Post.objects.all()

  return render(request, 'news/index.html',  {
    "news": news
  })
