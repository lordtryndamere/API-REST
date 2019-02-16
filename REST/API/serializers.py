from rest_framework import serializers
from django.contrib.auth.models import  User

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):   # validate data contiene todos los campos que pusimos arriba, como diccionario.
        instance = User()  # instance igual al user que ya tiene django . siempre se pasa validate_data igual.
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance
    def validate_username(self,data):  # valida si el usuario existe con nombre de usuario
        users = User.objects.filter (username=data)
        if len(users) != 0 :
            raise serializers.ValidationError(" Este nombre de usuario ya existe, intrese uno nuevo ")

        else :
            return data


