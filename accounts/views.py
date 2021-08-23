from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


# Create your views here.

# --------Signup---------

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
