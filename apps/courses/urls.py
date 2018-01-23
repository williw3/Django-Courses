from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^create$', views.create),
	url(r'^remove/(?P<id>\d+)$', views.remove),
	url(r'^destroy/(?P<id>\d+)$', views.destroy),
]