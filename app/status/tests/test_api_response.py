import json
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from status import models
from status.api import serializers


CREATE_URL = reverse('status:create')
LIST_URL = reverse('status:list')
DETAIL = 'status:detail'
UPDATE = 'status:update'
DELETE = 'status:delete'


def sample_item(user, content='New content'):
    return models.Status.objects.create(user=user, content=content)


def detail_url(url, _id):
    """Return URL for detail status"""
    return reverse(url, args=[_id])


class ApiResponseTests(APITestCase):
    """Test CRUD in API"""

    @classmethod
    def setUpTestData(cls):
        payload = {
            'username': 'test',
            'email': 'test@example.com',
            'password': 'testpass',
        }
        cls.user = get_user_model().objects.create_user(**payload)
        cls.item = sample_item(cls.user)
        super().setUpTestData()

    def test_create_status(self):
        """Test create status"""
        payload = {
            'user': self.user.id,
            'content': 'Test content',
        }

        res = self.client.post(CREATE_URL, payload)

        item2 = models.Status.objects.get(content='Test content')
        serializer2 = serializers.StatusSerializer(item2)

        self.assertContains(res, payload.get('content'), status_code=201)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(serializer2.data, json.loads(res.content))

    def test_list_statuses(self):
        """Test list statuses"""
        payload = {
            'user': self.user,
            'content': 'Test content',
        }
        item = models.Status.objects.first()
        item2 = sample_item(**payload)

        res = self.client.get(LIST_URL)

        serializer = serializers.StatusSerializer(item)
        serializer2 = serializers.StatusSerializer(item2)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual([serializer.data, serializer2.data], json.loads(res.content))

    def test_detail_status(self):
        """Test detail status"""
        serializer = serializers.StatusSerializer(self.item)
        url = detail_url(DETAIL, self.item.id)

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, json.loads(res.content))

    def test_update_status(self):
        """Test update status"""
        payload = {'content': 'Update content', 'user': self.user.id}
        url = detail_url(UPDATE, self.item.id)

        res = self.client.put(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json().get('content'), payload.get('content'))
        # self.assertIn(payload, res.json())

    def test_delete_status(self):
        """Test update status"""
        url = detail_url(DELETE, self.item.id)

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
