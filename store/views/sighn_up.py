from django.shortcuts import render
from django.views import View
from store.models.sighn_up import Sighn_up

class Sigh_up(View):
    def get(self,request):
        return render(request,'sighn_up.html')

    def post(self,request):
        temp=False
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            sign=Sighn_up(name=name,email=email,password=password)
            temp=True
            sign.save()

        except:
            pass
        return render(request,'sighn_up.html',{'temp':temp})



