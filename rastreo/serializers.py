from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	username = serializers.CharField()
	password = serializers.CharField()

	def create(self, validate_data):
		instance = User()
		instance.username = validate_data.get('username')
		instance.set_password(validate_data.get('password'))
		instance.save()
		return instance

	def validate_username(self, data):
		qs = User.objects.filter(username__iexact=data)
		if qs.exists():
			raise serializers.ValidationError("Este nombre ya se está utilizando")
		else:
			return data