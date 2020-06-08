from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

UserModel = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user