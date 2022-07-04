from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from products.views import get_product, get_product_all

urlpatterns = [
    path('<int:id>', get_product, name = "get_product"),
    path('', get_product_all, name = "get_product_all"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

