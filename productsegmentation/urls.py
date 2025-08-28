from django.contrib import admin
from django.urls import path, include
from segmentation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('segmentation.urls')),
]
