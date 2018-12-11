from . import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api_producto_lista', views.ProductoSerializer)
router.register(r'api_tienda_lista', views.TiendaSerializer, basename='api')

app_name = 'api'

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns += staticfiles_urlpatterns()
