from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.test import Client

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.all().delete()
        Menu.objects.create(title="Gnocchi", price=15, inventory=25)
        Menu.objects.create(title="IceCream", price=8, inventory=100)
        Menu.objects.create(title="Bruschetta", price=8, inventory=40)
        
    def test_getall(self):
        c = Client()
        response = c.get('/restaurant/menu/')
        instances = [
            {'menu_id': 5, 'title': "Gnocchi", 'price': '15.00', 'inventory': 25},
            {'menu_id': 6, 'title': "Icecream", 'price': '8.00', 'inventory': 100},
            {'menu_id': 7, 'title': "Bruschetta", 'price': '8.00', 'inventory': 40}
        ]
        
        self.assertEqual(response.data, instances)