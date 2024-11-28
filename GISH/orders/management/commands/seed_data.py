from django.core.management.base import BaseCommand
from orders.models import User, ChainType, ChainLength, Material, FontStyle, Product, Order

class Command(BaseCommand):
    help = "Seed database with initial test data"

    def handle(self, *args, **kwargs):
        # Create users
        user1 = User.objects.create_user(username="john_doe", email="john@example.com", password="password123", phone_number="1234567890")
        user2 = User.objects.create_user(username="jane_doe", email="jane@example.com", password="password123", phone_number="0987654321")

        # Create chain types
        belcher = ChainType.objects.create(name="Belcher", price_modifier=10.00)
        oval = ChainType.objects.create(name="Oval", price_modifier=12.50)

        # Create chain lengths
        short = ChainLength.objects.create(length="16 inches", price_modifier=5.00)
        medium = ChainLength.objects.create(length="18 inches", price_modifier=7.50)
        long = ChainLength.objects.create(length="20 inches", price_modifier=10.00)

        # Create materials
        silver = Material.objects.create(name="Silver", price_modifier=15.00)
        gold = Material.objects.create(name="Gold", price_modifier=25.00)
        rose_gold = Material.objects.create(name="Rose Gold", price_modifier=20.00)

        # Create font styles
        script = FontStyle.objects.create(name="Script")
        bold = FontStyle.objects.create(name="Bold")

        # Create products
        product1 = Product.objects.create(
            custom_name="John's Necklace",
            chain_type=belcher,
            chain_length=short,
            material=silver,
            font_style=script,
        )
        product2 = Product.objects.create(
            custom_name="Jane's Necklace",
            chain_type=oval,
            chain_length=long,
            material=gold,
            font_style=bold,
        )

        # Create orders
        order1 = Order.objects.create(customer=user1, status="pending")
        order1.products.add(product1)

        order2 = Order.objects.create(customer=user2, status="shipped")
        order2.products.add(product2)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
