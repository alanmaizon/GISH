from django.urls import reverse
from django.test import TestCase
from .models import CustomUser, ChainType, ChainLength, Material, Product, FontStyle

class ProductModelTest(TestCase):

    def setUp(self):
        self.chain_type = ChainType.objects.create(type_name="Belcher", price=15.00)
        self.chain_length = ChainLength.objects.create(length="18 inches", price=7.00)
        self.material = Material.objects.create(material_name="Gold", price=20.00)
        self.font_style = FontStyle.objects.create(style_name="Script")


    def test_calculate_final_price(self):
        product = Product.objects.create(
            custom_name="Tested",
            chain_type=self.chain_type,
            chain_length=self.chain_length,
            material=self.material
        )
        product.calculate_final_price()
        product.save()  # Save the calculated price
        self.assertEqual(product.final_price, 42.00)  # 15 + 7 + 20

    def test_generate_stock_code(self):
        product = Product.objects.create(
            custom_name="Tested",
            chain_type=self.chain_type,
            chain_length=self.chain_length,
            material=self.material
        )
        product.generate_stock_code()
        product.save()  # Save the generated stock code
        self.assertEqual(product.stock_code, "BELCHER-18-INCHES-G")


class ProductViewTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testuser", password="password123")
        self.chain_type = ChainType.objects.create(type_name="Belcher", price=15.00)
        self.chain_length = ChainLength.objects.create(length="18 inches", price=7.00)
        self.material = Material.objects.create(material_name="Gold", price=20.00)
        self.font_style = FontStyle.objects.create(style_name="Script")  # Add font style

    def test_create_product(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(reverse('create_product'), {
            'custom_name': 'Test Necklace',
            'chain_type': self.chain_type.id,
            'chain_length': self.chain_length.id,
            'material': self.material.id,
            'font_style': self.font_style.id,  # Include font_style in the POST data
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Product.objects.count(), 1)
