from django.test import TestCase
from django.urls import reverse

from rastreo.models import Vehiculo
from django.contrib.auth.models import User

class VehiculosByUserListViewTest(TestCase):
    def setUp(self):
        print("TEST...")
        test_usuario1 = User.objects.create_user(username='usuario1', password='contrasenia1')
        test_usuario2 = User.objects.create_user(username='usuario2', password='contrasenia2')

        test_usuario1.save()
        test_usuario2.save()

        vehiculos_test = 20
        for vehiculo_test in range(vehiculos_test):
            if vehiculo_test % 2:
                el_usuario = test_usuario1
            else:
                el_usuario = test_usuario2
            Vehiculo.objects.create(placa='ASD123QWE', ultima_pos_lat=19.349, ultima_pos_long=-99.19, usuario= el_usuario)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('vehiculos'))
        self.assertRedirects(response, '/accounts/login/?next=/rastreo/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='usuario1', password='contrasenia1')
        response = self.client.get(reverse('vehiculos'))
        self.assertEqual(str(response.context['user']), 'usuario1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rastreo/vehiculo_list.html')