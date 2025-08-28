from django.shortcuts import render
from .models import Product
import math

def index(request):
    products = Product.objects.all().order_by('price')
    # price segmentation parameters
    price_segments = int(request.GET.get('price_segments', 3))
    size_segments = int(request.GET.get('size_segments', 3))

    prices = list(products.values_list('price', flat=True))
    sizes = list(products.values_list('size', flat=True))

    price_ranges = []
    size_ranges = []

    if prices:
        min_p = float(min(prices))
        max_p = float(max(prices))
        step_p = (max_p - min_p) / price_segments if price_segments>0 else max_p - min_p
        for i in range(price_segments):
            low = min_p + i*step_p
            high = min_p + (i+1)*step_p if i < price_segments-1 else max_p
            price_ranges.append((round(low,2), round(high,2)))

    if sizes:
        min_s = int(min(sizes))
        max_s = int(max(sizes))
        step_s = math.ceil((max_s - min_s) / size_segments) if size_segments>0 else (max_s-min_s)
        for i in range(size_segments):
            low = min_s + i*step_s
            high = min_s + (i+1)*step_s - 1 if i < size_segments-1 else max_s
            size_ranges.append((low, high))

    # Build buckets
    price_buckets = []
    for pr in price_ranges:
        bucket_products = products.filter(price__gte=pr[0], price__lte=pr[1])
        price_buckets.append({'range': pr, 'count': bucket_products.count(), 'items': bucket_products})

    size_buckets = []
    for sr in size_ranges:
        bucket_products = products.filter(size__gte=sr[0], size__lte=sr[1])
        size_buckets.append({'range': sr, 'count': bucket_products.count(), 'items': bucket_products})

    context = {
        'products': products,
        'price_buckets': price_buckets,
        'size_buckets': size_buckets,
        'price_segments': price_segments,
        'size_segments': size_segments,
    }
    return render(request, 'segmentation/products.html', context)
