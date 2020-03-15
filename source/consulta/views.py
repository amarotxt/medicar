from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from consulta.models import Consulta
from consulta.serializers import ConsultaSerializer
# Create your views here.

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    

    def list(self, request):
        #  - Regra de negocio para
        # para nao exibir consultas de 
        # dia e horarios passados
        # -Os itens da listagem devem vir 
        # ordenados por ordem crescente 
        # do dia e horário da consulta
        
        date_now =  datetime.now().date()
        queryset = self.filter_queryset(self.get_queryset()).filter(dia__gte=date_now).order_by('-data_agendamento','horario')
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

        # return super().list(request)

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