from django.test import TestCase
from django.urls import reverse
from rest_framework import status, test
from .models import Question


# Create your tests here.
class TestQuestions(TestCase):

    def setUp(self):
        self.client = test.APIClient()
        self.data = {
                "title": "Test Question",
                "content": "This is a question to test the endpoint"
            }

    def test_create_questions(self):
        response = self.client.post(
            reverse('create_question'),
            data=self.data,
            format="json"
        )

        record = Question.objects.get(title="Test Question")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(record.title, self.data['title'])
