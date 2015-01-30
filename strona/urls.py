from django.conf.urls import url, patterns
from . import views


urlpatterns = [
               url(r'^/*$', views.index, name='index'),
               url(r'^post/(?P<id>\d+)/*$', views.post_show, name='post_show'),
]
