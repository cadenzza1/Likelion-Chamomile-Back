from django.contrib import admin
from .models import Product, Tag, Shop, Category, SubCategory, Review, Keyword, KeywordReview

admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Review)
admin.site.register(Keyword)
admin.site.register(KeywordReview)