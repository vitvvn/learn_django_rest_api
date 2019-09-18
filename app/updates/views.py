import json
from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
from django.views.generic import View

from app.mixins import JsonResponseMixin
from updates import models


# noinspection PyUnusedLocal
def json_example_view(request):
    data = {
        'count': 1000,
        'content': 'Some new content',
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'Some new content',
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'Some new content',
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, id, *args, **kwargs):
        obj = models.Update.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializeListView(View):
    # noinspection PyUnusedLocal
    def get(self, request, *args, **kwargs):
        qs = models.Update.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')
