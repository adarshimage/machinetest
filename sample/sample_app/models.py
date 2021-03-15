from django.db import models

# Create your models here.


class shop_details(models.Model):
    shop_name = models.CharField(max_length=250)
    shop_location = models.CharField(max_length=250)
    def __str__(self):
        return self.shop_name

class category_details(models.Model):
    category = models.CharField(max_length=250)
    def __str__(self):
        return self.category

class product_details(models.Model):
    shop_id = models.ForeignKey(shop_details,on_delete=models.CASCADE)
    cat_id = models.ForeignKey(category_details,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    product_image = models.ImageField(upload_to="product")


