from django.test import TestCase
from orders.models import Product, ChainType, ChainLength, Material, FontStyle

class ProductModelTest(TestCase):
    def setUp(self):
        self.chain_type = ChainType.objects.create(type_name="Belcher", price=15.00)
        self.chain_length = ChainLength.objects.create(length="18 inches", price=7.00)
        self.material = Material.objects.create(material_name="Silver", price=10.00)
        self.font_style = FontStyle.objects.create(style_name="Script")

    def test_calculate_final_price(self):
        product = Product(
            custom_name="Test",
            chain_type=self.chain_type,
            chain_length=self.chain_length,
            material=self.material,
            font_style=self.font_style
        )
        product.calculate_final_price()
        self.assertEqual(product.final_price, 32.00)

    def test_generate_stock_code(self):
        product = Product(
            custom_name="Test",
            chain_type=self.chain_type,
            chain_length=self.chain_length,
            material=self.material,
            font_style=self.font_style
        )
        product.generate_stock_code()
        self.assertEqual(product.stock_code, "BELCHER-18-INCHES-S")
