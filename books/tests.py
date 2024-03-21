from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Book 1",
            subtitle="Subtitle of book 1",
            author="Behrooz",
            isbn="12341234"
        )

    def test_api_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
