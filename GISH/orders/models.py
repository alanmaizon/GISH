from django.conf import settings
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    # Add related_name attributes to avoid clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username


class ChainType(models.Model):
    name = models.CharField(max_length=100)
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ChainLength(models.Model):
    length = models.CharField(max_length=100)
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.length


class Material(models.Model):
    name = models.CharField(max_length=100)
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class FontStyle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    custom_name = models.CharField(max_length=200)
    chain_type = models.ForeignKey(ChainType, on_delete=models.CASCADE, related_name="products")
    chain_length = models.ForeignKey(ChainLength, on_delete=models.CASCADE, related_name="products")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="products")
    font_style = models.ForeignKey(FontStyle, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")

    def final_price(self):
        """
        Calculate the final price dynamically based on the base price and modifiers.
        """
        return (
            self.base_price
            + self.chain_type.price_modifier
            + self.chain_length.price_modifier
            + self.material.price_modifier
        )

    def __str__(self):
        return self.custom_name


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('returned', 'Returned'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    products = models.ManyToManyField(Product, related_name="orders")

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"


# Message Model
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"