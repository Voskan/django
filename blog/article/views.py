from django.shortcuts import render
from .models import Article
import random

def index(req):
  articles = Article.objects.all()
  return render(req, 'article/index.html', {
    "articles": articles
  })

def article(req, id):
  article = Article.objects.get(pk=id)

  return render(req, 'article/article.html', {
    "article": article
  })


def contact(req):
  return render(req, 'static/contact.html')


def add_data(req):
  random_data = str(random.randrange(1, 100))

  Article.objects.create(
    title="My news title " + random_data,
    short_description="My news short description text " + random_data,
    description="My news description full text " + random_data,
    photo="test.jpeg",
    is_published=True,
  )
  return render(req, 'static/contact.html')