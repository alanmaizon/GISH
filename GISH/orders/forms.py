from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Product, Message

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['custom_name', 'chain_type', 'chain_length', 'material', 'font_style']
        widgets = {
            'custom_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'chain_type': forms.Select(attrs={'class': 'form-select'}),
            'chain_length': forms.Select(attrs={'class': 'form-select'}),
            'material': forms.Select(attrs={'class': 'form-select'}),
            'font_style': forms.Select(attrs={'class': 'form-select'}),
        }

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(required=False, max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))