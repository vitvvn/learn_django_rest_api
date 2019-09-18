from django.conf.urls import url, include
from django.contrib import admin
from updates import views


urlpatterns = [
    url(r'json/', views.json_example_view,),
    url(r'cbv/', views.JsonCBV.as_view()),
    url(r'cbv2/', views.JsonCBV2.as_view()),
    url(r'serialized_detail/(?P<id>.+)/$', views.SerializedDetailView.as_view()),
    url(r'serialized_list/', views.SerializeListView.as_view())
]
