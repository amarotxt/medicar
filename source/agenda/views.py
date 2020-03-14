from django.shortcuts import render
from rest_framework import viewsets
from agenda.models import Agenda
from agenda.serializers import AgendaSerializer
# Create your views here.

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


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