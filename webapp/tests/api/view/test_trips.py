from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


class UserRegisterTest(APITestCase):
    PASSWORD = 'pAssw0rd!'

    def test_given_same_password_and_confirm_password_204(self):
        url = reverse("v1:user-list")

        data = {
            'username': 'user@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': self.PASSWORD,
            'confirm_password': self.PASSWORD,
        }
        self.response = self.client.post(url, data)

        user = get_user_model().objects.first()

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(self.response.json()['username'], user.username)
        self.assertEqual(self.response.json()['first_name'], user.first_name)
        self.assertEqual(self.response.json()['last_name'], user.last_name)

        assert self.response.json().get("password") is None
        assert self.response.json().get("confirm_password") is None
