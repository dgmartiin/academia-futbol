from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from jugadores.models import Jugador


class Command(BaseCommand):

    help = 'Crea jugadores de ejemplo para la academia'

    def handle(self, *args, **kwargs):

        usuario, creado = User.objects.get_or_create(
            username='entrenador',
            defaults={
                'email': 'entrenador@academiafutbol.cl',
            }
        )

        if creado:
            usuario.set_password('Entrenador123!')
            usuario.save()

        jugadores = [
            {
                'nombre': 'Mateo González',
                'numero': 1,
                'posicion': 'Portero',
                'categoria': 'Sub-15',
                'nacionalidad': 'Chile',
                'url_imagen': 'https://images.unsplash.com/photo-1517466787929-bc90951d0974',
                'descripcion': 'Portero joven con buenos reflejos y gran capacidad para ordenar la defensa.',
                'activo': True,
            },
            {
                'nombre': 'Lucas Fernández',
                'numero': 2,
                'posicion': 'Defensa',
                'categoria': 'Sub-15',
                'nacionalidad': 'España',
                'url_imagen': 'https://images.unsplash.com/photo-1579952363873-27f3bade9f55',
                'descripcion': 'Defensa rápido y disciplinado, con buen juego defensivo.',
                'activo': True,
            },
            {
                'nombre': 'Diego Morales',
                'numero': 3,
                'posicion': 'Defensa',
                'categoria': 'Sub-17',
                'nacionalidad': 'Chile',
                'url_imagen': 'https://images.unsplash.com/photo-1553778263-73a83bab9b0c',
                'descripcion': 'Defensor fuerte físicamente y con buena salida desde el fondo.',
                'activo': True,
            },
            {
                'nombre': 'Álvaro Ruiz',
                'numero': 4,
                'posicion': 'Defensa',
                'categoria': 'Sub-17',
                'nacionalidad': 'España',
                'url_imagen': 'https://images.unsplash.com/photo-1579952363873-27f3bade9f55',
                'descripcion': 'Jugador defensivo con buena anticipación y lectura del juego.',
                'activo': True,
            },
            {
                'nombre': 'Tomás Herrera',
                'numero': 5,
                'posicion': 'Mediocampista',
                'categoria': 'Sub-17',
                'nacionalidad': 'Chile',
                'url_imagen': 'https://images.unsplash.com/photo-1526232761682-d26e03ac148e',
                'descripcion': 'Mediocampista con buena visión de juego y precisión en los pases.',
                'activo': True,
            },
            {
                'nombre': 'Sergio Martín',
                'numero': 6,
                'posicion': 'Mediocampista',
                'categoria': 'Sub-19',
                'nacionalidad': 'España',
                'url_imagen': 'https://images.unsplash.com/photo-1526232761682-d26e03ac148e',
                'descripcion': 'Volante creativo con capacidad para generar oportunidades.',
                'activo': True,
            },
            {
                'nombre': 'Nicolás Soto',
                'numero': 7,
                'posicion': 'Delantero',
                'categoria': 'Sub-15',
                'nacionalidad': 'Chile',
                'url_imagen': 'https://images.unsplash.com/photo-1579952363873-27f3bade9f55',
                'descripcion': 'Delantero rápido, habilidoso y con buen remate.',
                'activo': True,
            },
            {
                'nombre': 'Hugo Navarro',
                'numero': 8,
                'posicion': 'Mediocampista',
                'categoria': 'Sub-19',
                'nacionalidad': 'España',
                'url_imagen': 'https://images.unsplash.com/photo-1526232761682-d26e03ac148e',
                'descripcion': 'Mediocampista con gran resistencia y capacidad de recuperación.',
                'activo': True,
            },
            {
                'nombre': 'Gabriel Torres',
                'numero': 9,
                'posicion': 'Delantero',
                'categoria': 'Juvenil',
                'nacionalidad': 'Chile',
                'url_imagen': 'https://images.unsplash.com/photo-1517466787929-bc90951d0974',
                'descripcion': 'Delantero con gran definición dentro del área.',
                'activo': True,
            },
            {
                'nombre': 'Daniel López',
                'numero': 10,
                'posicion': 'Mediocampista',
                'categoria': 'Juvenil',
                'nacionalidad': 'España',
                'url_imagen': 'https://images.unsplash.com/photo-1526232761682-d26e03ac148e',
                'descripcion': 'Jugador técnico, creativo y con buen control del balón.',
                'activo': True,
            },
            {
                'nombre': 'Javier Castro',
                'numero': 11,
                'posicion': 'Delantero',
                'categoria': 'Sub-17',
                'nacionalidad': 'Chile',
                'url_imagen': 'https://images.unsplash.com/photo-1579952363873-27f3bade9f55',
                'descripcion': 'Extremo veloz con buen uno contra uno.',
                'activo': True,
            },
            {
                'nombre': 'Pablo Sánchez',
                'numero': 12,
                'posicion': 'Portero',
                'categoria': 'Sub-19',
                'nacionalidad': 'España',
                'url_imagen': 'https://images.unsplash.com/photo-1517466787929-bc90951d0974',
                'descripcion': 'Portero con buenos reflejos y seguridad bajo los tres palos.',
                'activo': True,
            },
            {
                'nombre': 'Andrés Rojas',
                'numero': 13,
                'posicion': 'Defensa',
                'categoria': 'Juvenil',
                'nacionalidad': 'Chile',
                'url_imagen': 'https://images.unsplash.com/photo-1553778263-73a83bab9b0c',
                'descripcion': 'Defensa completo, fuerte en los duelos y ordenado tácticamente.',
                'activo': True,
            },
            {
                'nombre': 'Mario Vidal',
                'numero': 14,
                'posicion': 'Mediocampista',
                'categoria': 'Sub-15',
                'nacionalidad': 'España',
                'url_imagen': 'https://images.unsplash.com/photo-1526232761682-d26e03ac148e',
                'descripcion': 'Mediocampista joven con gran potencial de crecimiento.',
                'activo': True,
            },
            {
                'nombre': 'Cristóbal Reyes',
                'numero': 15,
                'posicion': 'Delantero',
                'categoria': 'Sub-19',
                'nacionalidad': 'Chile',
                'url_imagen': 'https://images.unsplash.com/photo-1517466787929-bc90951d0974',
                'descripcion': 'Atacante potente con buen juego aéreo y definición.',
                'activo': True,
            },
            {
                'nombre': 'Alejandro Martín',
                'numero': 16,
                'posicion': 'Defensa',
                'categoria': 'Juvenil',
                'nacionalidad': 'España',
                'url_imagen': 'https://images.unsplash.com/photo-1553778263-73a83bab9b0c',
                'descripcion': 'Defensa polivalente que puede jugar en varias posiciones.',
                'activo': True,
            },
        ]

        creados = 0

        for datos in jugadores:
            jugador, creado = Jugador.objects.get_or_create(
                nombre=datos['nombre'],
                defaults={
                    **datos,
                    'autor': usuario,
                }
            )

            if creado:
                creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Se crearon {creados} jugadores correctamente.'
            )
        )