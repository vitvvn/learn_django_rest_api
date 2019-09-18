from django.http import JsonResponse


class JsonResponseMixin:
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    # noinspection PyMethodMayBeStatic
    def get_data(self, context):
        return context
