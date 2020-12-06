# Generated by Django 3.0.6 on 2020-12-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_catergory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='product_subcatergory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
