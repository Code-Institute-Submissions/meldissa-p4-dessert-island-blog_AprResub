from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.detail_url = reverse('post_detail', args=['test-slug'])
        self.like_url = reverse('post_like', args=['test-slug'])
        self.about_url = reverse('about')
        self.search_url = reverse('search')

    def test_post_list_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_like_GET(self):
        response = self.client.get(self.like_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_about_GET(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_search_GET(self):
        response = self.client.get(self.search_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
