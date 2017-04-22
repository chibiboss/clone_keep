#Urls de app landing
from django.conf.urls import url
from .views import index,agregar,detalle

urlpatterns = [
    url(r'^$',index, name = "index"),
    url(r'^agregar/$',agregar, name="agregar"),
    url(r'^detalle/(?P<pk>[0-9]+)/$',detalle, name="detalle"),

]