from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_materiales, name='materiales'),
    path('crear/', views.crear_material, name='crear_material'),
    path('<int:id>/', views.detalle_material, name='detalle_material'),
    path('editar/<int:id>/', views.editar_material, name='editar_material'),
    path('eliminar/<int:id>/', views.eliminar_material, name='eliminar_material'),

    path('agregar-sesion/<int:id>/', views.agregar_sesion, name='agregar_sesion'),
    path('lista-sesion/', views.lista_sesion, name='lista_sesion'),
    path('vaciar-sesion/', views.vaciar_sesion, name='vaciar_sesion'),
]