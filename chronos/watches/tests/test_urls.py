from django.test import SimpleTestCase
from django.urls import reverse, resolve

from chronos.watches.views import add_watch, show_all_watches, show_my_watches, show_watch, edit_watch, delete_watch, \
    like_watch


class TestUrls(SimpleTestCase):
    def test_add_watch_url_resolves(self):
        url = reverse('watches:add_watch')
        self.assertEqual(resolve(url).func, add_watch)

    def test_show_all_watches_url_resolves(self):
        url = reverse('watches:show_all_watches')
        self.assertEqual(resolve(url).func, show_all_watches)

    def test_show_collection_url_resolves(self):
        url = reverse('watches:show_collection')
        self.assertEqual(resolve(url).func, show_my_watches)

    def test_show_watch_url_resolves(self):
        test_id = 10
        url = reverse('watches:show_watch', args=[test_id])
        self.assertEqual(resolve(url).func, show_watch)

    def test_edit_watch_url_resolves(self):
        test_id = 10
        url = reverse('watches:edit_watch', args=[test_id])
        self.assertEqual(resolve(url).func, edit_watch)

    def test_delete_watch_url_resolves(self):
        test_id = 10
        url = reverse('watches:delete_watch', args=[test_id])
        self.assertEqual(resolve(url).func, delete_watch)

    def test_like_watch_url_resolves(self):
        test_id = 10
        url = reverse('watches:like_watch', args=[test_id])
        self.assertEqual(resolve(url).func, like_watch)
