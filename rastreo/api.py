from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from .serializers import UserSerializer, VehiculoSerializer
from .models import Vehiculo

class UserAPI(APIView):
	permission_classes = []
	def post(self, request):
		serializer = UserSerializer( data = request.data )
		if serializer.is_valid():
			user = serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED )
		else:
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST )

class VehiculoAPIView(generics.CreateAPIView):
	lookup_field = 'pk'
	serializer_class = VehiculoSerializer

	def get_queryset(self):
		return Vehiculo.objects.all()

	def perform_create(self, serializer):
		serializer.save(usuario=self.request.user)

class VehiculoRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = VehiculoSerializer

	def get_queryset(self):
		return Vehiculo.objects.all()