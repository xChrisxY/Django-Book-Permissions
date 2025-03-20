from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'password', 'names', 'last_names', 'age', 'active', 'admin']
        extra_kwargs = {'password': {'write_only': True}}

        
class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField()
    password = serializers.CharField()

    
class PasswordSerializer(serializers.Serializer):
    
    current_password = serializers.CharField()
    new_password = serializers.CharField()
