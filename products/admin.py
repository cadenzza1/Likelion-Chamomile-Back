from django.contrib import admin
from .models import Product, Filter, Shop, Category, SubCategory, Review, Keyword, KeywordReview

admin.site.register(Product)
admin.site.register(Filter)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Review)
admin.site.register(Keyword)
admin.site.register(KeywordReview)