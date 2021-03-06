from django.db import models

class Post(models.Model):
   title = models.CharField(max_length=150)
   content = models.TextField(blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   photo = models.ImageField(upload_to='photos/news/%Y/%m/%d/')
   is_published = models.BooleanField(default=False)