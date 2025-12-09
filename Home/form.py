from django import forms
from . models import CustomersInfo

class Order(forms.ModelForm):
    class Meta:
        model=CustomersInfo
        fields= "__all__"