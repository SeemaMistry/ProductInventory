from django.db import models
from products.models import Product

# Create your models here.
class Inventory(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE,)
    count = models.IntegerField(default=0)
    location = models.CharField(max_length=30)


    def __str__(self):
        return self.product.name + " " + str(self.count)