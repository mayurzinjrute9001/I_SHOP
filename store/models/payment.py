from django.db import models
from .product import Product
from .sighn_up import Sighn_up

class Payment(models.Model):
    order_id = models.CharField(max_length=30,null=False)
    payment_id = models.CharField(max_length=50)
    user = models.ForeignKey(Sighn_up, on_delete=models.CASCADE)
    product =models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
