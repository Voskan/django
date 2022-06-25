from statistics import mode
from django.db import models

class Article(models.Model):
  def __str__(self):
   return self.title

  class Meta:
    verbose_name = 'Article'
    verbose_name_plural = 'Articles'

  title = models.CharField(max_length=80)
  short_description = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  photo = models.ImageField(upload_to='photos/article/%Y/%m/%d/')
  is_published = models.BooleanField(default=False)
  views = models.IntegerField(blank=True, default=0)
  likes = models.IntegerField(blank=True, default=0)
  dis_likes = models.IntegerField(blank=True, default=0)