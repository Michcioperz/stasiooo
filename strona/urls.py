from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^/*$', views.index, name='index'),
    url(r'^post/(?P<pid>\d+)/*$', views.post_show, name='post_show'),
]
