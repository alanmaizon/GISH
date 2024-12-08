from django.core.management import call_command
from django.test import TestCase
from orders.models import ChainType

class SeedDataCommandTest(TestCase):
    def test_seed_data_command(self):
        call_command('seed_data')
        chain_types = ChainType.objects.all()
        self.assertTrue(chain_types.exists())
        self.assertIn("Belcher", [ct.type_name for ct in chain_types])
