import json
from django.test import TestCase, Client


class APITestCase(TestCase):

    c = Client()

    def assert_status_true(self, response):
        data = json.loads(response.content)
        status = data.get('status')
        self.assertTrue(status)

    def assert_status_false(self, response):
        data = json.loads(response.content)
        status = data.get('status')
        self.assertFalse(status)
