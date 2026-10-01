from django.urls import path

from .views import (
    JugadorList,
    JugadorDetail,
    JugadorCreate,
    JugadorUpdate,
    JugadorDelete,
    crear_jugador,
    registro,
)


urlpatterns = [
    path(
        '',
        JugadorList.as_view(),
        name='jugador_list'
    ),

    path(
        '<int:pk>/',
        JugadorDetail.as_view(),
        name='jugador_detail'
    ),

    path(
        'nuevo/',
        JugadorCreate.as_view(),
        name='jugador_create'
    ),

    path(
        '<int:pk>/editar/',
        JugadorUpdate.as_view(),
        name='jugador_update'
    ),

    path(
        '<int:pk>/borrar/',
        JugadorDelete.as_view(),
        name='jugador_delete'
    ),

    path(
        'nuevo/funcion/',
        crear_jugador,
        name='jugador_create_funcion'
    ),

    path(
        'registro/',
        registro,
        name='registro'
    ),
]