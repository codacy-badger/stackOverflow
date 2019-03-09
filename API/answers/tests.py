from django.test import TestCase
from rest_framework import test, status
from django.urls import reverse


# Create your tests here.
class TestAnswers(TestCase):

    def setUp(self):
        self.client = test.APIClient()

    def test_create_answers(self):
        response = self.client.post(
            reverse('create'),
            data={
                "content": "This is the test content"
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
