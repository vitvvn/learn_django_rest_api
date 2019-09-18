import json
from django.conf import settings
from django.db import models


def upload_update_image(instance, filename):
    return f'updates/{instance.user}/{filename}'


class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(self.values('user', 'content', 'image'))
        return json.dumps(list_values)


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def serialize(self):

        image = self.image.url if self.image else ''

        data = {
            'user': self.user.id,
            'content': self.content,
            'image': image
        }

        return json.dumps(data)

    def __str__(self):
        return self.content or ""
