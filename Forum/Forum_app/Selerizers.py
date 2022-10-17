from rest_framework import serializers
from .models import User


class Serializers:

    class UserCreate(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'

    class ValidatorUser(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'