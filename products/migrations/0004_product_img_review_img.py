# Generated by Django 4.0.5 on 2022-07-03 18:13

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_keyword_keywordreview_love_delete_tagreview_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, upload_to='product/img'),
        ),
        migrations.AddField(
            model_name='review',
            name='img',
            field=models.ImageField(blank=True, upload_to=products.models.get_review_img_path),
        ),
    ]