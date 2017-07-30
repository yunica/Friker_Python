from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^agregar/$', views.agregar, name='agregar'),
    url(r'^mostrar/$', views.mostrar, name='mostrar'),
    url(r'^mostrar2/(?P<pedido>[0-9]+)/$', views.mostrar2, name='mostrarmuchos'),
    url(r'^formulario/$', views.mostrarformulario, name='mostrarformulario'),
]

