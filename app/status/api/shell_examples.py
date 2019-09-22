import os
import django
from django.conf import settings
# from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()
settings.DEBUG = False

print(settings.INSTALLED_APPS)

from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from status.api.serializers import StatusSerializer
from status.models import Status


# get_user_model().objects.create_user(
#     username='test',
#     email='test@example.com',
#     password='testpass'
# )

# data = {
#     'user': 1,
#     'content': 'Content'
# }
obj = Status.objects.first()
serializer = StatusSerializer(obj)
print(serializer.data)
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
print(stream)
data = JSONParser().parse(stream)
print(data)
#
print('-------------------------------')
qs = Status.objects.all()
serializer = StatusSerializer(qs, many=True)
print(serializer.data)
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
print(stream)
data = JSONParser().parse(stream)
print(data)
#
# data = {'user': 1, 'content': 'New content'}
# serializer = StatusSerializer(data=data)
# serializer.is_valid()
# serializer.save()
#
obj = Status.objects.get(id=2)
print(obj)
data = {'content': 'New', 'user': 1}
serializer = StatusSerializer(instance=obj, data=data)
serializer.is_valid()
serializer.save()
