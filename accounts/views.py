from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
# from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


# Create your views here.

# --------Signup---------

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()  # Query to get all objects
    serializer_class = RegisterSerializer  # serializer class
    permission_classes = [IsAuthenticated]  # Permissions
    authentication_classes = [SessionAuthentication]  # Session-Authentication
    # authentication_classes = [TokenAuthentication]  # Token-Authentication
