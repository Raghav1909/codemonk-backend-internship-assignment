from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User

class RegisterUserView(APIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.create(serializer.validated_data)
        return Response(user_data, status=201)


class VerifyEmailView(APIView):
    def get(self, request, token):
        try:
            token_obj = Token.objects.get(key=token)
            user = User.objects.get(email=token_obj.user_id)

            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({'message': 'Email verified successfully'})
            
            else:
                return Response({'message': 'Email already verified'})

        except Token.DoesNotExist:
            return Response({'message': 'Invalid token'}, status=400)