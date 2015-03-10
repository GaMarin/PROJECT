from django.test import TestCase
from django.contrib.auth import get_user_model
#from .models import Entry



# Create your tests here.
class ViewTests(TestCase):
    def test_feed_url(self):
        response = self.client.get('/feed/')
        self.assertIn("xml", response['Content-Type'])
        raise notimplementedError#error a proposito