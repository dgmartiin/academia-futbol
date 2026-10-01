from django import forms
from .models import Jugador


class JugadorForm(forms.ModelForm):

    class Meta:
        model = Jugador
        fields = [
            'nombre',
            'numero',
            'posicion',
            'categoria',
            'nacionalidad',
            'url_imagen',
            'descripcion',
            'activo',
        ]

    def clean_url_imagen(self):
        url = self.cleaned_data['url_imagen']

        if not url.startswith('https://'):
            raise forms.ValidationError(
                'La URL de la imagen debe comenzar con https://'
            )

        return url