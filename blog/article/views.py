from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Article

def index(req):
  search = req.GET.get('search_input')
  title = "Blog home page"

  if not search:
    search = ""
  else:
    title = search + " - Blog"


  articles = Article.objects.filter(is_published=True, title__contains=search)

  return render(req, 'article/index.html', {
    "articles": articles,
    "title": title,
    "search": search
  })

def article(req, id):
  article = Article.objects.get(pk=id)
  article.views = article.views + 1
  article.save()

  return render(req, 'article/article.html', {
    "article": article,
    "title": article.title
  })

def delete(_, id):
  article = Article.objects.filter(pk=id)
  article.delete()

  return HttpResponseRedirect('/')

def contact(req):
  return render(req, 'static/contact.html', {
    "title": "Contact page"
  })
