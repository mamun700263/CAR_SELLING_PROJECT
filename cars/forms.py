from django import forms
from .models import OrderCar


class CarOrderForm(forms.ModelForm):
    class Meta:
            model = OrderCar
            fields = ('quantity',)
    