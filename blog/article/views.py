from django.shortcuts import render

def index(req):
  return render(req, 'article/index.html')


def contact(req):
  return render(req, 'static/contact.html')