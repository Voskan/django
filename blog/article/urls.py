from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('article/<id>', article),
    path('delete/<id>', delete),
]
