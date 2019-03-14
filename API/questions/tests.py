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
        self.create = self.client.post(
            reverse('create_question'),
            data=self.data,
            format="json"
        )

        self.record = Question.objects.get(title="Test Question")

    def test_create_questions(self):
        self.assertEqual(self.create.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.record.title, self.data['title'])

    def test_read_specific_question(self):
        get_response = self.client.get(
            reverse(
                'question_details',
                kwargs={'pk': self.record.id}
            ),
            format="json"
        )

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_update_specific_question(self):
        put_response = self.client.put(
            reverse(
                'question_details',
                kwargs={'pk': self.record.id}
            ),
            data={
                "title": "New title",
                "content": "New content"
            },
            format="json"
        )

        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(put_response.data['title'], self.data['title'])
        self.assertEqual(put_response.data['title'], 'New title')

    def test_delete_specific_question(self):
        new_record = Question.objects.create(
            title="Should Delete",
            content="Please pass and delete me"
        )

        res_before = self.client.get(
            reverse(
                'question_details',
                kwargs={
                    "pk": new_record.id
                }
            ),
            format="json"
        )

        del_response = self.client.delete(
            reverse(
                'question_details',
                kwargs={'pk': new_record.id}
            ),
            format="json"
        )

        res_after = self.client.get(
            reverse(
                'question_details',
                kwargs={
                    "pk": new_record.id
                }
            ),
            format="json"
        )

        get_record_deleted = Question.objects.filter(title="Should Delete")

        self.assertFalse(get_record_deleted)
        self.assertEqual(res_before.status_code, status.HTTP_200_OK)
        self.assertEqual(res_after.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        self.record.delete()
