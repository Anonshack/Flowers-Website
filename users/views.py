from django.contrib.auth import logout
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializers, LoginSerializer
from rest_framework.views import APIView
User = get_user_model()


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializers


class LoginAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({"message": "You are logged out successfully"}, status=status.HTTP_200_OK)


class AllUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers


class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk', None)
        if user_id is not None:
            user = self.get_object()
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        else:
            return Response({"detail": "User ID is required."}, status=400)
