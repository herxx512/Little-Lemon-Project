from django.test import TestCase
from django.urls import reverse
from django.urls import reverse
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu

class MenuTestView(TestCase):
    
    def setUp(self):        
        self.item1 = Menu.objects.create(title='Burgers', price=8.15, inventory=50)    
        # self.item2 = Menu.objects.create(title='Fries', price=3.25, inventory=100)
        # self.item3 = Menu.objects.create(title='Wings', price=9.49, inventory=30)
    
    def test_getall(self):
        response = self.client.get(reverse('menu-items'))
        serializedMenuItems = MenuSerializer(Menu.objects.all())
        # self.assertEquals(response.data, serializedMenuItems)
        self.assertEquals(response.status_code, 200)