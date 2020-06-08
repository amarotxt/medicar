from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication, SessionAuthentication #, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from cliente.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken import views as auth_views
# Create your views here.


UserModel = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        if request.user.is_superuser:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

        queryset = UserModel.objects.get(username=request.user)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super().create(request)