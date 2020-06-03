from datetime import datetime
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from agenda.models import Agenda
from agenda.serializers import AgendaSerializer
from .filters import AgendaFilter
from consulta.models import Consulta

# Create your views here.

class AgendaRegrasdeNegocio(object):
    def list_rn(self, queryset):
        #Regra de negocio:
        # Ordenado por ordem crecente 
        queryset = queryset.order_by('dia')
        
        # TODO: Agendas para datas passadas ou que todos os seus
        # horários já foram preenchidos devem ser excluídas 
        # da listagem

        return queryset

    def retirar_horarios_listagem(self, data):
        # TODO: Horários dentro de uma agenda que já passaram ou
        #  que foram preenchidos devem ser excluídos da listagem
        
        return data

class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_class = AgendaFilter
    filter_backends = (DjangoFilterBackend, )
    # filterset_fields = ['medico', ]



    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        queryset = AgendaRegrasdeNegocio.list_rn(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        
        data = AgendaRegrasdeNegocio.retirar_horarios_listagem(serializer.data)
        
        return Response(data)
        