from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=300)
    product_catergory = models.CharField(max_length=50, default="")
    product_subcatergory = models.CharField(max_length=50, default="")
    product_price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to="shop/images", default="")
    publish_date = models.DateField()

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
