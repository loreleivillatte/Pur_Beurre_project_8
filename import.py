"""import requests
import django
from django.db import transaction
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'pur_beurre.settings'
django.setup()

from favorites.models import Product


url_off = "https://fr.openfoodfacts.org/cgi/search.pl?"
params = {
    'action': 'process',
    'search_terms': 'petits déjeuners',
    'tagtype_0': 'states',
    'tag_contains_0': 'contains',
    'tag_0': 'complete',
    'tagtype_1': 'categories',
    'tag_contains_1': 'snacks',
    'tag_1': 'complete',
    'tagtype_2': 'languages',
    'tag_contains_2': 'contains',
    'tag_2': 'fr',
    'sort_by': 'unique_scans_n',
    'page_size': '50',
    'axis_x': 'energy',
    'axis_y': 'products_n',
    'page': '1',
    'json': '1'
    }

response = requests.get(url_off, params)
data = response.json()
products = data['products']

for items in products:
    try:
        name = items['product_name']
        category = "snacks"
        grade = items['nutrition_grades']
        code = items['code']
        img = items['image_url']
        with transaction.atomic():
            new_product = Product.objects.create(
                generic=name, category=category, grade=grade, code=code, image=img
            )
            print('ok')
    except KeyError:
        continue"""
