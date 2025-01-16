from time import time

from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from store.models.product import Product
from store.models.sighn_up import Sighn_up
from store.models.payment import Payment
from store.models.order import Custumer_order
from django.utils.decorators import method_decorator
from store.middlewares.auth import auth_middleware
from i_shop.settings import *
import razorpay

client = razorpay.Client(auth=(KEY_ID,KEY_SECRET))
# client.timeout = 10  # Add timeout to prevent connection issues


class Order(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer_id=request.session.get('id')
        customer=Sighn_up.objects.get(id=customer_id)
        cart = request.session.get('cart')
        orders=Custumer_order.objects.filter(user=customer)
        action=request.GET.get('action')
        products = Product.get_product_By_ids(list(cart.keys()))
        amount = 0
        for product in products:
            amount += product.product_price


        order=None
        payment=None
        error=None
        if customer is None:
            return redirect('homepage')
        if action == 'create_payment':
            currency="INR"
            if customer != False:
                notes = {
                    "email":customer.email,
                    "name":f'{customer.name}'
                }
                receipt = f"I-SHOP-{int(time())}"
                order = client.order.create(
                    {
                        'receipt': receipt,
                        'notes': notes,
                        'amount': amount * 100,  # amount in paise
                        'currency': currency
                    }
                )
                print(order)
                    # Your existing code
                # except razorpay.errors.BadRequestError as e:
                #     print(f"Razorpay error: {e}")
                #     error = str(e)
                payment = Payment()
                payment.user = customer

                payment.order_id = order.get('id')
                payment.save()
                payment.product.set(products)
            else:
                return redirect('login')
        context = {
            "product":products,
            "order":order,
            "payment":payment,
            "user":customer,
            "error":error

        }
        return render(request, 'cart.html',context=context)



    def post(self, request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer = request.session.get('id')
        cart = request.session.get('cart')
        products =Product.get_product_By_ids(list(cart.keys()))
        for product in products:
            order = Custumer_order(product=product,
                                   user=Sighn_up(id=customer),
                                   quantity=cart.get(str(product.id)),
                                   price=product.product_price,
                                   address=address,
                                   phone=phone)
            order.save()

        request.session['cart']={}
        return redirect('order')
@csrf_exempt
def verifypayment(request):
    if request.method == 'POST':
        data = request.POST
        context = {}

        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            payment = Payment.objects.get(oredr_id =razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            payment.save()
            return redirect('order')
        except:
            return HttpResponse("invalid payment details")





