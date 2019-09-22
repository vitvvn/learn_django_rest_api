from django.test import TransactionTestCase
from django.contrib.auth import get_user_model
from django.forms import ValidationError

from status import models
from status import forms


class ModelTests(TransactionTestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@example.com',
            password='testpass'
        )

    def test_status_str(self):
        """Test the update string representation"""
        payload = {
            'user': self.user,
            'content': 'Content'
        }
        status = models.Status.objects.create(**payload)

        self.assertEqual(str(status), status.content)

    def test_form_on_len_content_data(self):
        """Test the content data < 100 characters accept"""
        payload = {
            'user': self.user.id,
            'content': 'Small content'
        }

        form = forms.StatusForm(payload)
        form.is_valid()
        form.save()

        self.assertEqual(form.cleaned_data.get('content'), payload.get('content'))

    def test_form_on_error_len_content_data(self):
        """Test the content data > 100 charters eject"""
        payload = {
            'user': self.user.id,
            'content':
                """qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
                   qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
                """
        }
        form = forms.StatusForm(payload)
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError, form.full_clean())

        self.assertIn('Content is too long', str(form.errors))
