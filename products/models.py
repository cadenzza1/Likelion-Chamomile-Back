import os.path
import uuid

from django.db import models
from django.contrib.auth import get_user_model


def get_review_img_path(obj, fname):
    return os.path.join(
        'reviews',
        obj.id,
        f'{uuid.uuid4}_{fname}')


class Shop(models.Model):
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 40,null = True, blank = True)
    address = models.CharField(max_length = 300, null = True, blank = True)
    latitude = models.DecimalField(max_digits = 8, decimal_places = 3, null = True, blank = True)
    longitude = models.DecimalField(max_digits = 8, decimal_places = 3, null = True, blank = True)
    starttime = models.TimeField(null = True, blank = True)
    endtime = models.TimeField(null = True, blank = True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model): # 검색결과창에서 누르는 태그필터!
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Category(models.Model):  # 빵
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SubCategory(models.Model):  # 소금빵
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model): # 제품관련 테이블
    name = models.CharField(max_length=50)
    likenum = models.IntegerField(default = 0, blank = True)
    price = models.IntegerField(default = 0)
    img = models.ImageField(blank=True, upload_to=f"product/img")
    description = models.CharField(max_length = 1000, default = '', blank = True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    tag_set = models.ManyToManyField(Tag, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_img_url(self):
        if not self.img:
            return ""
        return self.img.url


# 입력받을 때 사용자가 입력을 안 하면 blank, default 값이 있으면 Null true 는 없어야함 - 서로 모순
# DB에 없어도 되는 정보인거면 null


class Review(models.Model): # 손수 쓰는 리뷰
    content = models.CharField(max_length = 1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, upload_to=get_review_img_path)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_img_url(self):
        if not self.img:
            return ""
        return self.img.url


class Keyword(models.Model): # 키워드
    content = models.CharField(max_length = 20)
    type = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class KeywordReview(models.Model): # 키워드 누르는 리뷰
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Love(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Mingyu(models.Model):
    