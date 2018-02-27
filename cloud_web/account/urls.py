
from django.conf.urls import url
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r"^login/$", auth_views.login, {"template_name":"account/login.html"},name="user_login"),
    url(r'^logout/$', auth_views.logout,{"template_name":"account/logout.html"}, name='user_logout'),
]
