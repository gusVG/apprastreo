from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from rastreo.api import UserAPI, VehiculoAPIView, VehiculoRUDView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('rastreo/', include('rastreo.urls')),
	path('', RedirectView.as_view(url='rastreo/', permanent=True)),
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/', include('django.contrib.auth.urls')),
	path('api/test/crea_usuario/', UserAPI.as_view(), name="api_crea_usuario" ),
	path('api/test/vehiculos/', VehiculoAPIView.as_view(), name="api_crea_vehiculo" ),
	path('api/test/vehiculos/<int:pk>/', VehiculoRUDView.as_view(), name="api_vehiculo_rud" ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
