import json
from django.test import TransactionTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from updates import models

JSON_URL = reverse('updates:json')
# DETAIL_URL = reverse('updates:serialized_detail')
LIST_URL = reverse('updates:serialized_list')


def detail_url(_id):
    """Return URL for detail update"""
    return reverse('updates:serialized_detail', args=[_id])


def sample_item(user, content='New content'):
    return models.Update.objects.create(user=user, content=content)


class ResponseTests(TransactionTestCase):

    def setUp(self) -> None:
        payload = {
            'username': 'test',
            'email': 'test@example.com',
            'password': 'testpass',
        }
        self.user = get_user_model().objects.create_user(**payload)

        self.item = sample_item(self.user)

    def test_json_response(self):
        """Json example response"""
        payload = {
            'count': 1000,
            'content': 'Some new content'
        }
        res = self.client.get(JSON_URL)

        self.assertContains(res, json.dumps(payload), status_code=200)

    def test_serialized_detail(self):
        res = self.client.get(detail_url(self.item.id))

        self.assertContains(res, json.dumps({'user': self.item.user.id, 'content': self.item.content,
                                             'image': ''}))

    def test_serializer_list(self):
        payload = {
            'user': self.user,
            'content': 'Two content',
        }
        item = sample_item(**payload)
        res = self.client.get(LIST_URL)

        self.assertContains(res, json.dumps([{'user': self.item.user.id, 'content': self.item.content,
                                             'image': ''}, {'user': item.user.id, 'content': item.content,
                                             'image': ''}]))
