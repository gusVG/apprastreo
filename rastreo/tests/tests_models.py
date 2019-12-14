from django.test import TestCase
from django.contrib.auth.models import User
from rastreo.models import Vehiculo

class VehiculoModelTest(TestCase):
    def setUp(self):
        test_usuario = User.objects.create_user(username='usuario', password='contrasenia')
        test_usuario.save()
        Vehiculo.objects.create(placa='ASD123QWE', ultima_pos_lat=19.349, ultima_pos_long=-99.19, usuario=test_usuario)

    def test_placa_label(self):
        vehiculo = Vehiculo.objects.get(id=1)
        field_label = vehiculo._meta.get_field('placa').verbose_name
        self.assertEquals(field_label, 'placa')

    def test_placa_max_length(self):
        vehiculo = Vehiculo.objects.get(id=1)
        max_length = vehiculo._meta.get_field('placa').max_length
        self.assertEquals(max_length, 20)

    def test_object_str_is_placa(self):
        vehiculo = Vehiculo.objects.get(id=1)
        expected_object_name = '{0}'.format(vehiculo.placa)
        self.assertEquals(expected_object_name, str(vehiculo))

    def test_get_absolute_url(self):
        vehiculo = Vehiculo.objects.get(id=1)
        self.assertEquals(vehiculo.get_absolute_url(), '/rastreo/')