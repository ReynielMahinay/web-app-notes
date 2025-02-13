from django.contrib.auth.models import User
from rest_framework import serializers


''' this will convert the python object to JSON data to be used in 
the communication with other application. Also allow to take JSON data
and convert that into the python code'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
         #the write_only is to accept new user  input but not return password when the user info is given
        #So no one can read the password
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user