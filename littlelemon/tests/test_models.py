from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    
    def test_get_item(self):
        item = Menu.objects.create(title='Burgers', price=8.15, inventory=50)
        itemstr = str(item)
        self.assertEqual(itemstr, 'Burgers : 8.15')