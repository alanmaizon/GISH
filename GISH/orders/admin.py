from django.contrib import admin
from .models import (
    User,
    ChainType,
    ChainLength,
    Material,
    FontStyle,
    Product,
    Order,
    Message,
)

# Custom User Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)


# Chain Type Admin
@admin.register(ChainType)
class ChainTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_modifier')
    search_fields = ('name',)


# Chain Length Admin
@admin.register(ChainLength)
class ChainLengthAdmin(admin.ModelAdmin):
    list_display = ('length', 'price_modifier')
    search_fields = ('length',)


# Material Admin
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_modifier')
    search_fields = ('name',)


# Font Style Admin
@admin.register(FontStyle)
class FontStyleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('custom_name', 'chain_type', 'chain_length', 'material', 'font_style', 'final_price')
    search_fields = ('custom_name',)
    list_filter = ('chain_type', 'chain_length', 'material', 'font_style')

    def final_price(self, obj):
        return obj.final_price()
    final_price.short_description = "Final Price"


# Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date', 'status')
    search_fields = ('id', 'customer__username', 'customer__email')
    list_filter = ('status', 'order_date')
    filter_horizontal = ('products',)  # For ManyToManyField


# Message Admin
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp', 'is_archived')
    search_fields = ('sender__username', 'receiver__username', 'content')
    list_filter = ('is_archived', 'timestamp')
