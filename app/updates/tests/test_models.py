from django.test import TransactionTestCase
from django.contrib.auth import get_user_model

from updates import models


class ModelTests(TransactionTestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@example.com',
            password='testpass'
        )

    def test_update_str(self):
        """Test the update string representation"""
        payload = {
            'user': self.user,
            'content': 'Content'
        }
        update = models.Update.objects.create(**payload)

        self.assertEqual(str(update), update.content)
