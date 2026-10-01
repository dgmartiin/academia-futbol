from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from .forms import JugadorForm
from .models import Jugador


class JugadorModelTest(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username='testuser',
            password='Test1234!'
        )

    def test_crear_jugador(self):
        jugador = Jugador.objects.create(
            nombre='Jugador Test',
            numero=10,
            posicion='Delantero',
            categoria='Sub-19',
            nacionalidad='Chile',
            url_imagen='https://ejemplo.com/jugador.jpg',
            descripcion='Jugador creado para pruebas.',
            activo=True,
            autor=self.usuario
        )

        self.assertEqual(jugador.nombre, 'Jugador Test')
        self.assertEqual(jugador.numero, 10)
        self.assertEqual(jugador.autor, self.usuario)

    def test_editar_jugador(self):
        jugador = Jugador.objects.create(
            nombre='Jugador Original',
            numero=7,
            posicion='Delantero',
            categoria='Sub-19',
            nacionalidad='Chile',
            url_imagen='https://ejemplo.com/jugador.jpg',
            descripcion='Descripción original.',
            activo=True,
            autor=self.usuario
        )

        jugador.numero = 11
        jugador.nombre = 'Jugador Editado'
        jugador.save()

        jugador_actualizado = Jugador.objects.get(pk=jugador.pk)

        self.assertEqual(jugador_actualizado.numero, 11)
        self.assertEqual(
            jugador_actualizado.nombre,
            'Jugador Editado'
        )

    def test_borrar_jugador(self):
        jugador = Jugador.objects.create(
            nombre='Jugador Para Borrar',
            numero=9,
            posicion='Delantero',
            categoria='Sub-17',
            nacionalidad='Chile',
            url_imagen='https://ejemplo.com/jugador.jpg',
            descripcion='Jugador que será eliminado.',
            activo=True,
            autor=self.usuario
        )

        jugador_id = jugador.id

        jugador.delete()

        self.assertFalse(
            Jugador.objects.filter(id=jugador_id).exists()
        )


class JugadorViewTest(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username='testuser',
            password='Test1234!'
        )

        self.jugador_activo = Jugador.objects.create(
            nombre='Jugador Activo',
            numero=10,
            posicion='Delantero',
            categoria='Sub-19',
            nacionalidad='Chile',
            url_imagen='https://ejemplo.com/activo.jpg',
            descripcion='Jugador activo.',
            activo=True,
            autor=self.usuario
        )

        self.jugador_inactivo = Jugador.objects.create(
            nombre='Jugador Inactivo',
            numero=5,
            posicion='Defensa',
            categoria='Sub-17',
            nacionalidad='Chile',
            url_imagen='https://ejemplo.com/inactivo.jpg',
            descripcion='Jugador inactivo.',
            activo=False,
            autor=self.usuario
        )

    def test_lista_muestra_solo_activos(self):
        response = self.client.get(
            reverse('jugador_list')
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jugador Activo')
        self.assertNotContains(response, 'Jugador Inactivo')

    def test_usuario_autenticado_puede_crear(self):
        self.client.login(
            username='testuser',
            password='Test1234!'
        )

        datos = {
            'nombre': 'Nuevo Jugador',
            'numero': 8,
            'posicion': 'Mediocampista',
            'categoria': 'Sub-17',
            'nacionalidad': 'Chile',
            'url_imagen': 'https://ejemplo.com/nuevo.jpg',
            'descripcion': 'Nuevo jugador de prueba.',
            'activo': True,
        }

        response = self.client.post(
            reverse('jugador_create'),
            datos
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Jugador.objects.filter(
                nombre='Nuevo Jugador'
            ).exists()
        )

    def test_usuario_no_autenticado_no_puede_crear(self):
        response = self.client.get(
            reverse('jugador_create')
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn(
            '/accounts/login/',
            response.url
        )

    def test_usuario_autenticado_puede_editar(self):
        self.client.login(
            username='testuser',
            password='Test1234!'
        )

        datos = {
            'nombre': 'Jugador Modificado',
            'numero': 99,
            'posicion': 'Delantero',
            'categoria': 'Sub-19',
            'nacionalidad': 'Chile',
            'url_imagen': 'https://ejemplo.com/modificado.jpg',
            'descripcion': 'Jugador modificado.',
            'activo': True,
        }

        response = self.client.post(
            reverse(
                'jugador_update',
                kwargs={'pk': self.jugador_activo.pk}
            ),
            datos
        )

        self.assertEqual(response.status_code, 302)

        self.jugador_activo.refresh_from_db()

        self.assertEqual(
            self.jugador_activo.nombre,
            'Jugador Modificado'
        )

        self.assertEqual(
            self.jugador_activo.numero,
            99
        )

    def test_usuario_autenticado_puede_borrar(self):
        self.client.login(
            username='testuser',
            password='Test1234!'
        )

        response = self.client.post(
            reverse(
                'jugador_delete',
                kwargs={'pk': self.jugador_activo.pk}
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(
            Jugador.objects.filter(
                pk=self.jugador_activo.pk
            ).exists()
        )


class JugadorFormTest(TestCase):

    def test_form_rechaza_url_no_https(self):
        datos = {
            'nombre': 'Jugador Test',
            'numero': 10,
            'posicion': 'Delantero',
            'categoria': 'Sub-19',
            'nacionalidad': 'Chile',
            'url_imagen': 'http://ejemplo.com/foto.jpg',
            'descripcion': 'Jugador de prueba.',
            'activo': True,
        }

        form = JugadorForm(data=datos)

        self.assertFalse(form.is_valid())
        self.assertIn(
            'url_imagen',
            form.errors
        )


class JugadorCSRFTest(TestCase):

    def test_post_sin_csrf_devuelve_403(self):
        cliente = Client(enforce_csrf_checks=True)

        cliente.force_login(
            User.objects.create_user(
                username='csrfuser',
                password='Test1234!'
            )
        )

        datos = {
            'nombre': 'Jugador CSRF',
            'numero': 20,
            'posicion': 'Delantero',
            'categoria': 'Sub-19',
            'nacionalidad': 'Chile',
            'url_imagen': 'https://ejemplo.com/csrf.jpg',
            'descripcion': 'Prueba de CSRF.',
            'activo': True,
        }

        response = cliente.post(
            reverse('jugador_create'),
            datos
        )

        self.assertEqual(response.status_code, 403)