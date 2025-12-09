from django.urls import path
from . import views
urlpatterns = [
    path('',views.display),
    path('customer/',views.Customer,name='order'),
]
