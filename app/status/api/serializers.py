from rest_framework import serializers

from status.models import Status


# noinspection PyMethodMayBeStatic
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
        ]

    def validate_content(self, value):
        if len(value) > 240:
            raise serializers.ValidationError('Content is too long!')
        return value

    def validate(self, data):
        content = data.get('content', None)
        if content == '':
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Content or image is required!')
        return super().validate(data)
