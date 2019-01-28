from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from favorites.models import Product
import requests


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.product_1 = Product.objects.create(
            generic='product1', grade='b', code='123456', category='cat', image='https://aear.jpeg')
        self.product_2 = Product.objects.create(
            generic='product2', grade='a', code='45678', category='cat', image='https://bear.jpeg')
        self.user_input = 'product'
        self.user = User.objects.get_or_create(username='test_user')[0]
        self.detail_url = reverse('detail', args=[self.product_1.id])
        self.add_favorites_url = reverse('save', args=[self.product_1.id])
        self.results_url = reverse('results', args=[self.product_1.id, self.user_input])

    def test_index_GET(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorites/index.html')

    def test_search_POST(self):
        response = self.client.post(reverse('search'), kwargs={'query': self.user_input})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorites/index.html')

    def test_results_GET(self):
        response = self.client.get(self.results_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorites/results.html')

    def test_favorites_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('favorite'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorites/favorites_page.html')

    def test_add_favorites_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(self.add_favorites_url)
        self.assertEquals(response.status_code, 302)


class TestLogin(TestCase):
    def setUp(self):
        self.credentials = {'username': 'test_user', 'password': 'pass'}
        User.objects.create_user(**self.credentials)

    def test_login_valid_POST(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.assertEqual(response.status_code, 200)

    def test_login_invalid_POST(self):
        self.credentials = {'username': 'test_user', 'password': 'wrong'}
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertFalse(response.context['user'])
        self.assertEqual(response.status_code, 200)


class TestViewApi(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_1 = Product.objects.create(
            generic='product1', grade='b', code='3760020507350', category='cat', image='https://aear.jpeg')
        self.url_product = "https://fr.openfoodfacts.org/api/v0/produit/{}.json"
        self.data = requests.get(f"{self.url_product}{3760020507350}")

    def test_api_GET(self):
        self.result = self.data
        self.assertEqual(self.result.status_code, 200)

    def test_detail_GET(self):
        response = self.client.get(reverse('detail', args=[self.product_1.id]))
        self.assertTrue(response.context['product_selected'])
        self.assertEqual(response.status_code, 200)
