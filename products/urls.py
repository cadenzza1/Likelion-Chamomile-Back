from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import get_product, get_product_all, get_shop_info

urlpatterns = [
    # id 번호에 해당하는 row 가져와야 하기때문에 id필요한거고
    path('<int:id>', get_product, name = "get_product"), 
    # 전부 긁어올 거기 때문에 id값이 필요없다.
    path('', get_product_all, name = "get_product_all"),
    path('<int:product_id>/shop', get_shop_info, name= "get_shop_info")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

