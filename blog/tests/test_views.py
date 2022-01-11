from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment


class TestViews(TestCase):

    def test_post_list_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # def test_post_detail_GET(self):
    #     response = self.client.get(reverse('post_detail', args=['recipe1']))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_detail.html')

    # def test_post_like_GET(self):
    #     response = self.client.get(reverse('post_like', args=['recipe1']))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_detail.html')

    def test_about_GET(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_search_GET(self):
        response = self.client.get(reverse('search'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
