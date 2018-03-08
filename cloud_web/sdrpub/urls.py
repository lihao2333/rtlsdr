from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$", views.sdr_list, name="sdrpub_list"),
    url(r'(?P<sdr_ip>\d+.\d+.\d+.\d+)/$', views.sdr_detail, name="sdrpub_detail"),
    url(r'^register$', views.sdr_register, name="sdrpub_register"),
]