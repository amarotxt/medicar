from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication #, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from especialidade.models import Especialidade
from especialidade.serializers import EspecialidadeSerializer
# Create your views here.
from rest_framework import filters
    

class EspecialidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, )
    permission_classes = (IsAuthenticated, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']