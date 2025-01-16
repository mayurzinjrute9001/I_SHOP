"""
URL configuration for i_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.views.index import Index
from i_shop import settings
from django.conf.urls.static import static
from store.views.sighn_up import Sigh_up
from store.views.login import Login
from store.views import login
from store.views.cart import Cart
from store.views.order import Order
from store.views.order import verifypayment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index.as_view(),name='homepage'),
    path('sighnup/',Sigh_up.as_view(),name='sighnup'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',login.logout,name='logout'),
    path('cart/',Cart.as_view(),name='cart'),
    path('order/',Order.as_view(),name='order'),
    path('verify_payment',verifypayment,name='verify_payment')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
