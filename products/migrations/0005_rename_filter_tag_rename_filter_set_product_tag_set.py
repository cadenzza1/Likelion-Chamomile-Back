# Generated by Django 4.0.5 on 2022-07-03 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_img_review_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Filter',
            new_name='Tag',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='filter_set',
            new_name='tag_set',
        ),
    ]
