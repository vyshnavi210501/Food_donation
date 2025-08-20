from django.shortcuts import render
from rest_framework import generics
from .serializers import UserRegisterSerializer,UserLoginSerializer, UserProfileSerializer  
from .models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes=[]

class UserLoginView(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class = UserLoginSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes=[IsAuthenticated]