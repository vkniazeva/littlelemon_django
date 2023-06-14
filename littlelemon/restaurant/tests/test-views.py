from django.test import TestCase
from restaurant.views import MenuItemsView
from rest_framework.test import APIClient
from restaurant.models import Menu
from django.urls import reverse



def create_items(self):
        menu_item_list = []
        self.test_menu_1 = Menu.objects.create(title = 'MenuItem1', price = str('4.00'), inventory = '15')
        self.test_menu_2 = Menu.objects.create(title = 'MenuItem2', price = str('8.00'), inventory ='30')
        self.test_menu_3 = Menu.objects.create(title ='MenuItem3', price= str('12.00'), inventory ='45')
        menu_item_list.append(self.test_menu_1)
        menu_item_list.append(self.test_menu_2)
        menu_item_list.append(self.test_menu_3)
        
        return menu_item_list
    
class MenuViewTest(TestCase):  
    def setUp(self):
        self.client = APIClient()
        self.menu_item_list = create_items(self)
          
    def test_get_all(self):
        url = reverse('restaurant_menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        menu_expected_list = self.menu_item_list
        menu_result_list = response.data
        
        for i in range(len(menu_expected_list)):
            menu_exp = menu_expected_list[i]
            menu_res = menu_result_list[i]
            
            self.assertEqual(menu_exp.title, menu_res['title'])
            self.assertEqual(str(menu_exp.price), str(menu_res['price']))
            self.assertEqual(str(menu_exp.inventory), str(menu_res['inventory']))


        