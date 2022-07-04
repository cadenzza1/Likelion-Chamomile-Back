from products.models import Product
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

def home(request):
    return render(request,'home.html')
    
def get_product_all(request):
    if request.method == "GET":
        product_all = Product.objects.all()
        product_json_all = []

        for product in product_all:
            product_json = {
                "id" : product.id,
                "name" : product.name,
                "likenum" : product.likenum,
                "price" : product.price,
                "img" : product.img,
                "description" : product.description,
                "shop" : product.shop,
                "tag_set" : product.tag_set,
                "sub_category" : product.sub_category,
            }
            product_json_all.append(product_json)

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message":"생성 성공",
            "data" : product_json_all
        })

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