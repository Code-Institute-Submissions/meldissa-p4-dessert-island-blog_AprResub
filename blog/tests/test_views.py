from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.about_url = reverse('about')
        self.search_url = reverse('search')
        self.post_detail_url = reverse('post_detail', args=['recipe1'])
        self.post_like_url = reverse('post_like', args=['recipe1'])
        self.user = User.objects.create(username='testname')
        self.recipe = Post.objects.create(
            title='recipe1',
            author=self.user
        )

    def test_post_list_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_GET(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_search_GET(self):
        response = self.client.get(self.search_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    def test_post_detail_POST(self):
        response = self.client.post(self.post_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_like_POST(self):
        response = self.client.post(self.post_like_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
