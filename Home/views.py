from django.shortcuts import render
from .models import Products
from .form import LoginForm
# Create your views here.
def display(request):
    products=Products.objects.all()
    return render(request,'index.html',{'products':products})

def login(request):
    formObj=LoginForm()
    return render(request,'LoginForm.html',{'obj':formObj})