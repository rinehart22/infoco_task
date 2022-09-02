#from django.test import TestCase
from .models import *
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

User = get_user_model()


class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        user = User(username='srk', email='srk@gmail.com')
        user.set_password('password')
        user.save()
        blog_post = BlogPost.objects.create(
            user=user, title='sometittle', content='random_cont')

    def test_single_user(self):
        cnt = User.objects.count()
        self.assertEquals(cnt, 1)
