from django.contrib import admin
from . models import Products
class productAdmin(admin.ModelAdmin):
    list_display=('img','song')
# Register your models here.

admin.site.register(Products,productAdmin) 