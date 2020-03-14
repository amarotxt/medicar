from django.shortcuts import render
from rest_framework import viewsets
from especialidade.models import Especialidade
from especialidade.serializers import EspecialidadeSerializer
# Create your views here.

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = especialidade.objects.all()
    serializer_class = EspecialidadeSerializer


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