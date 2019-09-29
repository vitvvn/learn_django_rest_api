import json
from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response

from status.models import Status
from status.api import serializers


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

# class StatusListSearchApiView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = serializers.StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = serializers.StatusSerializer(qs, many=True)
#         return Response(serializer.data)


class StatusCreateApiView(generics.CreateAPIView, ):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class StatusApiView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = serializers.StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StatusDetailApiView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer
    # lookup_field = 'id'

    # def get_object(self):
    #     key = self.kwargs.get('sample')
    #     obj = Status.objects.get(id=key)
    #     return obj


class StatusUpdateApiView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer


class StatusDeleteApiView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer


# noinspection PyRedeclaration
class StatusApiAllView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView
):
    passed_id = None
    permission_classes = []
    authentication_classes = []
    serializer_class = serializers.StatusSerializer

    @staticmethod
    def func_passed_id(request):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_passed_id or new_passed_id or None

        return passed_id

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id
        print(request.body)

        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        self.passed_id = passed_id = self.func_passed_id(request)
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.passed_id = self.func_passed_id(request)
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.passed_id = self.func_passed_id(request)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.passed_id = self.func_passed_id(request)
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

