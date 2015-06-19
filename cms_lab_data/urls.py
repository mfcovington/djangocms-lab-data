from django.conf.urls import url

from .views import (DataFileDetailView, DataFileListView,
    DataFileSetDetailView, DataFileSetListView)

urlpatterns = [
    url(r'^files/$', DataFileListView.as_view(), name='data_file_list'),
    url(r'^files/(?P<slug>[-\w]+)/$', DataFileDetailView.as_view(), name='data_file_detail'),
    url(r'^sets/$', DataFileSetListView.as_view(), name='data_file_set_list'),
    url(r'^sets/(?P<slug>[-\w]+)/$', DataFileSetDetailView.as_view(), name = 'data_file_set_detail'),
]
