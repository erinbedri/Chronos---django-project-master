from django.test import SimpleTestCase
from django.urls import reverse, resolve

from chronos.web.views import show_homepage


class TestUrls(SimpleTestCase):
    def test_show_homepage_url_resolves(self):
        url = reverse('web:show_homepage')
        self.assertEqual(resolve(url).func, show_homepage)

