from django.test import TransactionTestCase
from django.contrib.auth import get_user_model

from status import models


def sample_item(user, content='New content'):
    return models.Update.objects.create(user=user, content=content)


class ResponseTests(TransactionTestCase):

    def setUpTestData(self) -> None:
        payload = {
            'username': 'test',
            'email': 'test@example.com',
            'password': 'testpass',
        }
        self.user = get_user_model().objects.create_user(**payload)

        self.item = sample_item(self.user)
