from django.urls import path

from . import views

urlpatterns = [
	path('', views.VehiculoListView.as_view(), name='vehiculos'),
	path('vehiculo/create/', views.VehiculoCreate.as_view(), name='vehiculo_create'),
    path('vehiculo/<int:pk>/update/', views.VehiculoUpdate.as_view(), name='vehiculo_update'),
    path('vehiculo/<int:pk>/delete/', views.VehiculoDelete.as_view(), name='vehiculo_delete'),
]