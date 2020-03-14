from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from especialidade.models import Especialidade
from especialidade.serializers import EspecialidadeSerializer
# Create your views here.
from rest_framework import filters

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
    
    def list(self, request):
        return super().list(request)

    def create(self, request):
        return super().create(request)

    def retrieve(self, request, pk=None):
        return super().retrieve(request)

    def update(self, request, pk=None):
        return super().update(request)

    def partial_update(self, request, pk=None):
        return super().partial_update(request)

    def destroy(self, request, pk=None):
        return super().destroy(request)