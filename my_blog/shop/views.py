from django.shortcuts import render

def index(request):
  d = [
    {
      "id": 1,
      "name": "MacBook ipsum dolor sit amet consectetur.",
      "price": 2560,
      "count": 12,
      "image": "hp.webp",
      "categories": ["Electronics", "Computers", "Tools"]
    },
    {
      "id": 2,
      "name": "HP ipsum dolor sit amet consectetur.",
      "price": 1500,
      "count": 10,
      "image": "zenbook.webp",
      "categories": ["Computers", "Tools"]
    },
    {
      "id": 3,
      "name": "DELL ipsum dolor sit amet consectetur.",
      "price": 1200,
      "count": 13,
      "image": "hp.webp",
      "categories": ["Electronics", "Tools"]
    },
    {
      "id": 4,
      "name": "ASUS ipsum dolor sit amet.",
      "price": 1100,
      "count": 18,
      "image": "zenbook.webp",
      "categories": ["Electronics", "Computers"]
    }
  ]

  return render(request, 'shop/index.html', {
    "products": d,
    "hello": "Barev"
  })


def product(request):
  product = [{
    "id": 1,
    "name": "MacBook ipsum dolor sit amet consectetur.",
    "price": 2560,
    "count": 12,
    "image": "hp.webp",
    "categories": ["Electronics", "Computers", "Tools"],
    "availability": "In stock",
    "brand": "ASUS",
    "screen_size": 14,
    "screen_type": "TN",
    "resolution": {"width": 1366, "height": 768},
    "processor": "Intel Core",
    "cpu": "Intel Celeron N4020",
    "processor_cache": 8
  }]
  
  return render(request, 'shop/product.html', {
    "products": product
  })