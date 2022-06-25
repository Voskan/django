from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('add-data/', add_data),
    path('article/<id>', article),
]
