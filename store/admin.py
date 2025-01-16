from django.contrib import admin
from store.models.product import Product
from store.models.category import Category
from store.models.sighn_up import Sighn_up
from store.models.order import Custumer_order
from store.models.payment import Payment



# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sighn_up)
admin.site.register(Custumer_order)
admin.site.register(Payment)


