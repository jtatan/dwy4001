from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from apps.compra.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^.*$', IndexView.as_view(), name='index'),
    url(r'^compra/', include('apps.compra.urls', namespace="compra")),
    url(r'^accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('',include('pwa.urls')),

]
