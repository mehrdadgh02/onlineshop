from django import forms
from .models import Product


class OrderForm(forms.Form):
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple)
    delivery_time = forms.DateTimeField()
    recipient_name = forms.CharField(max_length=100)
