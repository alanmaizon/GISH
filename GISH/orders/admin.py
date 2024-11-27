from django.contrib import admin
from .models import Customer, ChainType, ChainLength, Material, FontStyle, Order, Product

admin.site.register(Customer)
admin.site.register(ChainType)
admin.site.register(ChainLength)
admin.site.register(Material)
admin.site.register(FontStyle)
admin.site.register(Order)
admin.site.register(Product)
