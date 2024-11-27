from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

# User Model
class Customer(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

# ChainType Model
class ChainType(models.Model):
    type_name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.type_name

# ChainLength Model
class ChainLength(models.Model):
    length = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.length

# Material Model
class Material(models.Model):
    material_name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.material_name

# FontStyle Model
class FontStyle(models.Model):
    style_name = models.CharField(max_length=255)

    def __str__(self):
        return self.style_name

# Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"

# Product Model
class Product(models.Model):
    custom_name = models.CharField(max_length=12)
    final_price = models.FloatField(null=True, blank=True)
    stock_code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    chain_type = models.ForeignKey(ChainType, on_delete=models.PROTECT)
    chain_length = models.ForeignKey(ChainLength, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    font_style = models.ForeignKey(FontStyle, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="products", blank=True, null=True)

    def calculate_final_price(self):
        self.final_price = (
            (self.chain_type.price if self.chain_type else 0) +
            (self.chain_length.price if self.chain_length else 0) +
            (self.material.price if self.material else 0)
        )

    def generate_stock_code(self):
        code_parts = [
            self.chain_type.type_name.upper() if self.chain_type else "",
            self.chain_length.length.replace(" ", "-").upper() if self.chain_length else "",
            self.material.material_name[0].upper() if self.material else ""
        ]
        self.stock_code = "-".join(code_parts)

    def save(self, *args, **kwargs):
        self.calculate_final_price()
        self.generate_stock_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.custom_name
