from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^compra/', include('apps.compra.urls', namespace="compra")),
    url(r'^accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('',include('pwa.urls')),

]
