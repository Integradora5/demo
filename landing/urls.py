from django.urls import path
from landing.views import index
from landing.views import nosotros
from landing.views import contacto



#crear un path por pestaña
urlpatterns=[ path("", index, name="index"),
             path("nosotros", nosotros, name="nosotros"),
             path("contacto", contacto, name="contacto"),
             ]
