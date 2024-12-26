from django.urls import path
from . import views

urlpatterns = [
    path('personas/',views.getPersona,name='get-personas'),
    path('personas/add',views.addPersona,name='add-persona'),
]
