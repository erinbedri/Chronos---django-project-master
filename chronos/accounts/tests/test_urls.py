from django.test import SimpleTestCase
from django.urls import reverse, resolve

from chronos.accounts.views import register_account, login_user, show_account, edit_account, delete_account, logout_user


class TestUrls(SimpleTestCase):
    def test_register_account_url_resolves(self):
        url = reverse('accounts:register_account')
        self.assertEqual(resolve(url).func, register_account)

    def test_login_user_url_resolves(self):
        url = reverse('accounts:login_account')
        self.assertEqual(resolve(url).func, login_user)

    def test_show_account_url_resolves(self):
        url = reverse('accounts:show_account')
        self.assertEqual(resolve(url).func, show_account)

    def test_edit_account_url_resolves(self):
        url = reverse('accounts:edit_account')
        self.assertEqual(resolve(url).func, edit_account)

    def test_delete_account_url_resolves(self):
        url = reverse('accounts:delete_account')
        self.assertEqual(resolve(url).func, delete_account)

    def test_logout_user_url_resolves(self):
        url = reverse('accounts:logout_account')
        self.assertEqual(resolve(url).func, logout_user)
