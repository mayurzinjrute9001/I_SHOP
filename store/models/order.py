import datetime

from django.db import models
from .product import Product
from .sighn_up import Sighn_up


class Custumer_order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(Sighn_up,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='')
    phone = models.CharField(max_length=20,default='')
    date = models.DateTimeField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)
    @staticmethod
    def get_order_by_customer(customer):
        return Custumer_order.objects.filter(user=customer)

