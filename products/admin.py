from django.contrib import admin
from .models import Product, Filter, Shop, Category, SubCategory, Review, TagReview


admin.site.register(Product) # 기본 ModelAdmin으로 등록
admin.site.register(Filter)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Review)
admin.site.register(TagReview)

