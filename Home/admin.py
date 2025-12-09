from django.contrib import admin
from . models import Products,CustomersInfo
class productAdmin(admin.ModelAdmin):
    list_display=('img','song')
class orderAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','location','payment','age')

# Register your models here.

admin.site.register(Products,productAdmin) 
admin.site.register(CustomersInfo,orderAdmin)