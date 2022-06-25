from django.db import models

class Article(models.Model):
  title = models.CharField(max_length=80)
  short_description = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  photo = models.ImageField(upload_to='photos/article/%Y/%m/%d/')
  is_published = models.BooleanField(default=False)