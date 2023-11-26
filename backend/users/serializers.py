from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.response import Response
from .models import User
from .tasks import send_verification_email
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all(), message="Email already exists")])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['email', 'password']


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, is_verified=False)
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        send_verification_email.delay(user.email, token.key)
        return {
            'email': user.email,
            'token': token.key
        }