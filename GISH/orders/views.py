from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .forms import CustomUserCreationForm, ProductForm, LoginForm
from .models import Product, Order, Message

def home(request):
    """
    Home view for the main page.
    """
    products = Product.objects.all()
    return render(request, 'orders/home.html', {'products': products})

def create_product(request):
    """
    View for creating a product with customization options.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            # Redirect to an order summary page or another view
            return redirect('order_summary')
    else:
        form = ProductForm()
    return render(request, 'orders/product_form.html', {'form': form})

def register(request):
    """
    User registration view.
    """
    if request.user.is_authenticated:
        return redirect(reverse('home'))  # Redirect already logged-in users
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect(reverse('home'))
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # You can customize the redirect URL based on your needs
                return redirect('home')  # Replace 'home' with your desired URL name
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    """
    User logout view.
    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect(reverse('login'))

@login_required
def user_orders(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'orders/user_orders.html', {'orders': orders})


@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'orders/inbox.html', {'messages': received_messages})