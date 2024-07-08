from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model=User       # tell the serializer to use the User model which contains all usernames, emails ......
        fields=['id','username','password','email']         #fields that we want to use 