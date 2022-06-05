from itertools import count
from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=80)
  price = models.IntegerField()
  count = models.SmallIntegerField()
  availability = models.BooleanField(default=True)
  description = models.TextField()
  processor = models.CharField(max_length=20)
  cpu = models.CharField(max_length=20)
  processor_cache = models.SmallIntegerField()
  screen_type = models.CharField(max_length=20)
  screen_size = models.SmallIntegerField()
  brand = models.CharField(max_length=20)