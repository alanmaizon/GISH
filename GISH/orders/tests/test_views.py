from django.test import TestCase
from django.urls import reverse
from orders.models import User

class CustomizationViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_customization_view_unauthenticated(self):
        response = self.client.get(reverse("customization"))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_customization_view_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("customization"))
        self.assertEqual(response.status_code, 200)

