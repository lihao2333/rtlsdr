from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$", views.sdr_list, name="sdr_list"),
    url(r'(?P<sdr_id>\d)/$', views.sdr_detail, name="sdr_detail"),
]