from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import JugadorForm
from .models import Jugador


class JugadorList(ListView):
    model = Jugador
    template_name = 'jugadores/jugador_list.html'
    context_object_name = 'jugadores'
    paginate_by = 12

    def get_queryset(self):
        return Jugador.objects.filter(activo=True)


class JugadorDetail(DetailView):
    model = Jugador
    template_name = 'jugadores/jugador_detail.html'
    context_object_name = 'jugador'


class JugadorCreate(LoginRequiredMixin, CreateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'jugadores/jugador_form.html'
    success_url = reverse_lazy('jugador_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class JugadorUpdate(LoginRequiredMixin, UpdateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'jugadores/jugador_form.html'

    def get_success_url(self):
        return reverse_lazy(
            'jugador_detail',
            kwargs={'pk': self.object.pk}
        )


class JugadorDelete(LoginRequiredMixin, DeleteView):
    model = Jugador
    template_name = 'jugadores/jugador_confirm_delete.html'
    success_url = reverse_lazy('jugador_list')


@login_required
def crear_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)

        if form.is_valid():
            jugador = form.save(commit=False)
            jugador.autor = request.user
            jugador.save()

            return render(
                request,
                'jugadores/jugador_detail.html',
                {'jugador': jugador}
            )

    else:
        form = JugadorForm()

    return render(
        request,
        'jugadores/jugador_form.html',
        {'form': form}
    )


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)

            return redirect('jugador_list')

    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/registro.html',
        {'form': form}
    )


@require_POST
def cerrar_sesion(request):
    logout(request)
    return redirect('jugador_list')