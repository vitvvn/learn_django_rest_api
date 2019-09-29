from django.conf.urls import url
from status.api import views

app_name = 'status'

"""CRUD"""
urlpatterns = [
    url(r'create/$', views.StatusCreateApiView.as_view(), name='create'),
    url(r'^$', views.StatusApiView.as_view(), name='list'),
    url(r'all/$', views.StatusApiAllView.as_view(), name='all'),
    url(r'(?P<pk>\d+)/$', views.StatusDetailApiView.as_view(), name='detail'),
    url(r'(?P<pk>\d+)/update/$', views.StatusUpdateApiView.as_view(), name='update'),
    url(r'(?P<pk>\d+)/delete/$', views.StatusDeleteApiView.as_view(), name='delete'),

]
