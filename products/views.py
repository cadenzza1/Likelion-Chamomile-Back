from unicodedata import name
from products.models import Product
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
from django.views import View
from .models import Category, Product, Shop
# Create your views here.

def home(request):
    return render(request,'home.html')

def get_product_all(request):
    category_name = request.GET.get('name', None)
    
    if request.method == "GET":
        product_all = Product.objects.filter(name__contains = category_name)
        product_json_all = []

        for product in product_all:
            product_json = {
                "id" : product.id,
                "name" : product.name,
                "likenum" : product.likenum,
                "price" : product.price,
                "img" : product.get_img_url(),
                "description" : product.description,
                "shop" : product.shop.name,
                "tag_set" : list(product.tag_set.values()),
                "sub_category" : product.sub_category.name,
            }
            product_json_all.append(product_json)

        json_res = json.dumps(
            {
            "status" : 200,
            "success" : True,
            "message": "생성 성공",
            "data" : product_json_all
            },
        ensure_ascii=False
        )
        
        return HttpResponse(
                json_res,
                content_type=u"application/json; charset=utf-8",
                status = 200,
            )

def get_product(request, id):
    if request.method == "GET":
        product = get_object_or_404(Product, pk = id)
        product_json = {
            "id" : product.id,
            "name" : product.name,
            "likenum" : product.likenum,
            "price" : product.price,
            "img" : product.get_img_url(),
            "description" : product.description,
            "shop" : product.shop.name,
            "tag_set" : list(product.tag_set.values()),
            "sub_category" : product.sub_category.name,
        }

        json_res = json.dumps(
            {
            "status" : 200,
            "success" : True,
            "message": "생성 성공",
            "data" : product_json
            },
            ensure_ascii=False
        )
        return HttpResponse(
                json_res,
                content_type=u"application/json; charset=utf-8",
                status = 200,
            )

def get_shop_info(request,product_id):
    if request.method == "GET":
        product = get_object_or_404(Product, pk = product_id)
        product_review = product.review_set.all()
        shop = get_object_or_404(Shop, pk = product.shop.id)
        all_products_of_the_shop = Product.objects.filter(shop_id = product.shop.id)
        product_json_all = []
        for product in all_products_of_the_shop:
            product_json = {
                "id" : product.id,
                "name" : product.name,
                "likenum" : product.likenum,
                "price" : product.price,
                "img" : product.get_img_url(),
                "description" : product.description,
                "shop" : product.shop.name,
                "tag_set" : list(product.tag_set.values()),
                "sub_category" : product.sub_category.name,
            }
            product_json_all.append(product_json)

        shop_json = {
            "id" : shop.id,
            "shop_name" : shop.name,
            "all_products_of_the_shop" : product_json_all,
            "latitude" : shop.latitude,
            "gyungdo" : shop.longitude,
            "phone" : shop.phone,
            "address" : shop.address,
            "start_time" : shop.starttime.strftime('%h:%M'),
            "end_time" : shop.endtime.strftime('%h:%M'),
            "product_review" : product_review,
        }

        json_res = json.dumps(
            {
            "status" : 200,
            "success" : True,
            "message": "생성 성공",
            "data" : shop_json
            },
            ensure_ascii=False
        )
        return HttpResponse(
                json_res,
                content_type=u"application/json; charset=utf-8",
                status = 200,
            )