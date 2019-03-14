from django.test import TestCase
from rest_framework import test, status
from django.urls import reverse
from questions.models import Question


# Create your tests here.
class TestAnswers(TestCase):

    def setUp(self):
        self.client = test.APIClient()

    def test_create_answers(self):
        question = Question.objects.create()
        response = self.client.post(
            reverse('create_answer'),
            data={
                "content": "This is the test content",
                "question": question.pk
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
