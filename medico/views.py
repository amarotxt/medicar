from django.shortcuts import render
from rest_framework import viewsets
from medico.models import Medico
from medico.serializers import MedicoSerializer
# Create your views here.

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = medico.objects.all()
    serializer_class = MedicoSerializer


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