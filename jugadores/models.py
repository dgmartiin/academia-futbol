from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Jugador(models.Model):

    POSICIONES = [
        ('Portero', 'Portero'),
        ('Defensa', 'Defensa'),
        ('Mediocampista', 'Mediocampista'),
        ('Delantero', 'Delantero'),
    ]

    CATEGORIAS = [
        ('Sub-15', 'Sub-15'),
        ('Sub-17', 'Sub-17'),
        ('Sub-19', 'Sub-19'),
        ('Juvenil', 'Juvenil'),
    ]

    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    posicion = models.CharField(
        max_length=20,
        choices=POSICIONES
    )
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )
    nacionalidad = models.CharField(max_length=50)
    url_imagen = models.URLField()
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'

    def __str__(self):
        return f'{self.nombre} - #{self.numero}'

    def get_absolute_url(self):
        return reverse(
            'jugador_detail',
            kwargs={'pk': self.pk}
        )