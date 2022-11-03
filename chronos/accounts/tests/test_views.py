from datetime import datetime

from django import test as django_test
from django.contrib.auth import get_user_model, login
from django.urls import reverse

from chronos.watches.models import Watch

UserModel = get_user_model()


class ShowAccountTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qwe',
    }

    VALID_WATCH_DATA = {
        'brand': 'Test Brand',
        'model': 'Test Model',
        'style': 'Pocket',
    }

    @staticmethod
    def _create_user(**credentials):
        return UserModel.objects.create_user(**credentials)

    def test_expect_correct_template(self):
        user = self._create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.client.get(reverse('accounts:show_account'))
        self.assertTemplateUsed('accounts/details.html')

    def test_show_account__when_new_user_logged_in__expect_watch_count_to_be_0(self):
        user = self._create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.client.get(reverse('accounts:show_account'))
        self.assertEqual(response.context['watch_count'], 0)

    def test_show_account__when_user_logged_in_and_has_watch_expect_watch_count_to_be_correct(self):
        user = self._create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)

        watch = Watch.objects.create(
            **self.VALID_WATCH_DATA,
            owner=user,
        )

        response = self.client.get(reverse('accounts:show_account'))
        self.assertEqual(response.context['watch_count'], 1)

    def test_show_account__when_new_user_logged_in__expect_total_paid_to_be_0(self):
        user = self._create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.client.get(reverse('accounts:show_account'))
        self.assertEqual(response.context['total_paid'], 0)

    def test_show_account__when_user_logged_in_and_has_watch_expect_expect_total_paid_to_be_correct(self):
        user = self._create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)

        watch = Watch.objects.create(
            **self.VALID_WATCH_DATA,
            owner=user,
            price_paid=1000,
        )

        response = self.client.get(reverse('accounts:show_account'))
        self.assertEqual(response.context['total_paid'], 1000)
