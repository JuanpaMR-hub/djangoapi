from django.urls import path
from rest_framework import routers
from . import views,api

router = routers.DefaultRouter()

router.register('api/personas',api.PersonaViewSet,'personas')

urlpatterns = [
    path('',views.home, name = 'home')
]

urlpatterns += router.urls