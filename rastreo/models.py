from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User

class Vehiculo(models.Model):
    """
    Modelo que representa un vehiculo.
    """
    placa = models.CharField(max_length=20, help_text="Introduce Placa")
    ultima_pos_lat = models.DecimalField(max_digits=11, decimal_places=7, help_text="Introduce Última latitud")
    ultima_pos_long = models.DecimalField(max_digits=12, decimal_places=7, help_text="Introduce Última longitud")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """
        String para identificar Vehiculo a traves de placa
        """
        return self.placa

    def get_absolute_url(self):
        return reverse('vehiculos')