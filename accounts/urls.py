from django.conf.urls import url
from . import views

app_nme = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup"),
]