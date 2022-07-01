from ctypes import addressof
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    likenum = models.IntegerField(default = 0, blank = True)
    price = models.IntegerField(default = 0)
    # img = models.ImageField 나중에 합시다
    description = models.CharField(max_length = 1000, default = '', blank = True)

# 입력받을 때 사용자가 입력을 안 하면 blank, default 값이 있으면 Null true 는 없어야함 - 서로 모순
# DB에 없어도 되는 정보인거면 null

class Filter(models.Model): # 검색결과창에서 누르는 태그필터!
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    
class Shop(models.Model):
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 40,null = True, blank = True)
    address = models.CharField(max_length = 300, null = True, blank = True)
    latitude = models.DecimalField(max_digits = 8, decimal_places = 3, null = True, blank = True)
    longitude = models.DecimalField(max_digits = 8, decimal_places = 3, null = True, blank = True)
    starttime = models.TimeField(null = True, blank = True)
    endtime = models.TimeField(null = True, blank = True)
    
class Category(models.Model): # 빵
    name = models.CharField(max_length = 30)

class SubCategory(models.Model): # 소금빵
    name = models.CharField(max_length = 30)

class Review(models.Model): # 손수 쓰는 리뷰
    content = models.CharField(max_length = 1000)

class ReviewTag(models.Model): # 태그 누르는 리뷰
    color = models.CharField(max_length = 20)