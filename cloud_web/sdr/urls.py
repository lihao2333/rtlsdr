from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$", views.sdr_list, name="sdr_list"),
    url(r'(?P<sdr_ip>\d)/$', views.sdr_detail, name="sdr_detail"),
    url(r'^register$', views.sdr_register, name="sdr_register"),
]