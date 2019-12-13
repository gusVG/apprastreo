from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vehiculo

class VehiculoListView(LoginRequiredMixin, generic.ListView):
    model = Vehiculo
    template_name ='vehiculo/vehiculo_list.html'

    def get_queryset(self):
        return Vehiculo.objects.filter(usuario=self.request.user)

class VehiculoCreate(CreateView):
    model = Vehiculo
    fields = '__all__'

class VehiculoUpdate(UpdateView):
    model = Vehiculo
    fields = ['placa', 'ultima_pos_lat', 'ultima_pos_long', 'usuario']

class VehiculoDelete(DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('vehiculos')