# your test file
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class AnonUserTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_public_bookmarks(self):
        response = self.client.get('/api/v1/bookmarks/')
        assert response.status_code == 200

    def test_create_bookmark(self):
        response = self.client.post('/api/v1/bookmarks/')
        assert response.status_code == 401
