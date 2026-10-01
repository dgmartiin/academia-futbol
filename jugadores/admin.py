from django.contrib import admin
from .models import Jugador


@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'numero',
        'posicion',
        'categoria',
        'nacionalidad',
        'autor',
        'activo',
        'creado',
    )

    list_filter = (
        'posicion',
        'categoria',
        'activo',
    )

    search_fields = (
        'nombre',
        'nacionalidad',
        'descripcion',
    )

    ordering = (
        '-creado',
    )