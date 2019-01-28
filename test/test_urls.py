from django.test import SimpleTestCase
from django.urls import reverse, resolve
from favorites.views import index, legal
from favorites.views_account import registration, login_view, logout_view
from favorites.views_product import search, results, detail_product, save_substitute, favorites_page


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_legal_url_is_resolved(self):
        url = reverse('legal')
        print(resolve(url))
        self.assertEquals(resolve(url).func, legal)

    def test_registration_url_is_resolved(self):
        url = reverse('registration')
        print(resolve(url))
        self.assertEquals(resolve(url).func, registration)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_view)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_view)

    def test_search_url_is_resolved(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search)

    def test_results_url_is_resolved(self):
        url = reverse('results', args=['1', 'test'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, results)

    def test_detail_url_is_resolved(self):
        url = reverse('detail', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, detail_product)

    def test_save_url_is_resolved(self):
        url = reverse('save', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, save_substitute)

    def test_favorites_url_is_resolved(self):
        url = reverse('favorite')
        print(resolve(url))
        self.assertEquals(resolve(url).func, favorites_page)


