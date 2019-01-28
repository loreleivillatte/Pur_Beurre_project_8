from django.test import TestCase
from favorites.forms import RegistrationForm, AuthForm


class TestForms(TestCase):

    def test_registration_form_valid_data(self):
        form_data = {
            'username': 'registration1',
            'email': 'ad@mp.com',
            'password': 'registration3',
            'confirm_password': 'registration4'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid_data(self):
        form_data = {}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_auth_form_valid_data(self):
        form_data = {
            'username': 'auth1',
            'password': 'auth3',
        }
        form = AuthForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_auth_form_invalid_data(self):
        form_data = {}
        form = AuthForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

