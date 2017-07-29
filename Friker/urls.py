from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('FrikerApp.urls')),
    url(r'^fotoxx/', include('fotox.urls')),
    url(r'^admin/', admin.site.urls),
]
