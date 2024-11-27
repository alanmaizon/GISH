from django.core.management.base import BaseCommand
from orders.models import ChainType, ChainLength, Material, FontStyle

class Command(BaseCommand):
    help = 'Seed initial data for the database'

    def handle(self, *args, **kwargs):
        # Seed Chain Types
        ChainType.objects.get_or_create(type_name="Belcher", price=15.00)
        ChainType.objects.get_or_create(type_name="Oval", price=20.00)

        # Seed Chain Lengths
        ChainLength.objects.get_or_create(length="16 inches", price=5.00)
        ChainLength.objects.get_or_create(length="18 inches", price=7.00)
        ChainLength.objects.get_or_create(length="20 inches", price=9.00)

        # Seed Materials
        Material.objects.get_or_create(material_name="Silver", price=10.00)
        Material.objects.get_or_create(material_name="Gold", price=20.00)
        Material.objects.get_or_create(material_name="Rose Gold", price=18.00)

        # Seed Font Styles
        FontStyle.objects.get_or_create(style_name="Script")
        FontStyle.objects.get_or_create(style_name="Bold")
        FontStyle.objects.get_or_create(style_name="Italic")

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
