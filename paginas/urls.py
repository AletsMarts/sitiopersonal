from django.urls import path
from .views import vista_pagina_inicio, about


urlpatterns = [
     path('', vista_pagina_inicio),
     path('nosotros/', about),
]