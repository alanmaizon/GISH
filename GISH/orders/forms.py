from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['custom_name', 'chain_type', 'chain_length', 'material', 'font_style']

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(required=False, max_length=15)

    class Meta:
        model = Customer
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
