from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registrarcliente/$', views.index, name='index'),
    url(r'^llogin/$', views.llogin, name='llogin'),
]