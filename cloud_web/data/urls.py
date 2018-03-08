from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.data_list, name="data_list"),
    url(r'(?P<data_id>\d+)/$', views.data_detail, name="data_detail"),
    url(r'^upload$', views.data_upload, name="data_upload"),
    url(r'^get$', views.data_get, name="data_get"),
]