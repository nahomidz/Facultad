from os import name,path
from django.conf.urls import url,include
from django.urls import path
from .views import index, coment, listado

urlpatterns = [
    path('',index, name="index"),
    path('comentario/',coment, name="comentario"),
    path('lista/',listado, name="lista"),
    path('accounts/', include('django.contrib.auth.urls')),


]
