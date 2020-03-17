from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from medico.models import Medico
from medico.serializers import MedicoSerializer


# Create your views here.

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, )
    search_fields = ['nome']
    filterset_fields = ['especialidade']

    def list(self, request):
        return super().list(request)

    def create(self, request):
        pass
    def retrieve(self, request, pk=None):
        return super().retrieve(request)
    def update(self, request, pk=None):
        pass
    def partial_update(self, request, pk=None):
        pass
    def destroy(self, request, pk=None):
        pass