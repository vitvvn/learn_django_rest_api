from django.conf.urls import url
from updates import views

app_name = 'updates'

urlpatterns = [
    url(r'json/', views.json_example_view, name='json', ),
    url(r'cbv/', views.JsonCBV.as_view(), name='cbv', ),
    url(r'cbv2/', views.JsonCBV2.as_view(), name='cbv2', ),
    url(r'serialized_detail/(?P<id>.+)/$', views.SerializedDetailView.as_view(), name='serialized_detail', ),
    url(r'serialized_list/', views.SerializeListView.as_view(), name='serialized_list', )
]
