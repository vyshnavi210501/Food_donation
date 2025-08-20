from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=('username', 'email', 'password', 'id')
    def create(self, validated_data):
        user=User.objects.create_user(validated_data['username'], validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','email','id')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username', 'email', 'id')
