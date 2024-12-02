from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .forms import CustomUserCreationForm, ProductForm, LoginForm, MessageForm, EmailChangeForm
from .models import Product, Order, Message, ChainType, ChainLength, Material
from django.http import JsonResponse


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
    form = ProductForm()
    return render(request, 'orders/product_form.html', {
        'form': form,
    })

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
    return render(request, 'orders/register.html', {'form': form})

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

    return render(request, 'orders/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def user_orders(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'orders/user_orders.html', {'orders': orders})


@login_required
def inbox(request):
    # Display received messages
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')

    # Handle sending new messages
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Set the sender as the logged-in user
            message.save()
            return redirect('inbox')  # Redirect to inbox after sending
    else:
        form = MessageForm()

    return render(request, 'orders/inbox.html', {'messages': messages, 'form': form})

@login_required
def change_email(request):
    user = request.user
    if request.method == 'POST':
        form = EmailChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('email_change_done')
    else:
        form = EmailChangeForm(instance=user)
    return render(request, 'orders/email_change.html', {'form': form})

@login_required
def email_change_done(request):
    return render(request, 'orders/email_change_done.html')

def get_price(request):
    item_type = request.GET.get('type')  # Type: 'chain_type', 'material', etc.
    item_id = request.GET.get('id')     # Selected item's ID

    price = 0.0
    if item_type == "chain_type":
        price = ChainType.objects.filter(id=item_id).values_list('price_modifier', flat=True).first()
    elif item_type == "chain_length":
        price = ChainLength.objects.filter(id=item_id).values_list('price_modifier', flat=True).first()
    elif item_type == "material":
        price = Material.objects.filter(id=item_id).values_list('price_modifier', flat=True).first()

    return JsonResponse({'price': price})
