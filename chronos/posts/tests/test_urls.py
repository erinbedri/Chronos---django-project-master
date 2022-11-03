from django.test import SimpleTestCase
from django.urls import reverse, resolve

from chronos.posts.views import PostListView, show_post


class TestUrls(SimpleTestCase):
    def test_show_all_posts_url_resolves(self):
        url = reverse('posts:show_posts')
        self.assertEqual(resolve(url).func.__name__, PostListView.as_view().__name__)

    def test_show_post_url_resolves(self):
        test_id = 10
        url = reverse('posts:show_post', args=[test_id])
        self.assertEqual(resolve(url).func, show_post)

