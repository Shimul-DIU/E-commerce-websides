from django.shortcuts import render,redirect
from .models import Products
from . form import Order
# Create your views here.
def display(request):
    products=Products.objects.all()
    return render(request,'index.html',{'products':products})
def Customer(request):
    if request.method=='POST':
       form=Order(request.POST)
       if form.is_valid():
           form.save()
          
    else:
        form=Order()
    return render(request,'order.html',{'form':form} )
