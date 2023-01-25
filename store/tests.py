import unittest
from typing import List

from django.test import Client

from .models import Category


class CategoryTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.url_category = '/api/store/category'
        self.category = Category.objects.create(title="Tortas")

    
    def tearDown(self):
        self.category.delete()
    
    def test_create_category(self):
        data = {'Sobremesas'}
        response = self.client.post(self.url_category, data)
        print("RESPONSE", response.json())
        self.assertEqual(response.status_code, 200)


    def test_get_categorys(self):
        response = self.client.get(self.url_category)
        self.assertEqual(response.status_code, 200)
 