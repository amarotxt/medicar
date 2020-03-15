from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from consulta.models import Consulta
from consulta.serializers import ConsultaSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        #  - Regra de negocio para
        # para nao exibir consultas de 
        # dia e horarios passados
        # -Os itens da listagem devem vir 
        # ordenados por ordem crescente 
        # do dia e horário da consulta
        
        date_now =  datetime.now().date()
        queryset = self.filter_queryset(self.get_queryset()).filter(agenda__dia__gte=date_now).order_by('-data_agendamento','horario')
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

        # return super().list(request)

    def create(self, request, *args, **kwargs):
        raise Exception(reques)
        return super().create(request)

    def delete(self, request, *args, **kwargs):
        raise Exception(reques)
        return super().create(request)

    