from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'^', include('FrikerApp.urls'), name='FrikerApp'),
    url(r'^fotox/', include('fotox.urls'), name='fotox'),
    url(r'^admin/', admin.site.urls),
]
