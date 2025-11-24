from django.urls import path
from . import views
urlpatterns = [
    path('',views.display),
    path('login/',views.login,name='login'),
]
