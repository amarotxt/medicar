from datetime import datetime
# from datetime import timedelta
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from agenda.models import Agenda
from agenda.serializers import AgendaSerializer
from .filters import AgendaFilter
from consulta.models import Consulta

# Create your views here.

class AgendaRegrasdeNegocio(object):
    def list_rn(self, queryset):
        #Regra de negocio:
        # Horários dentro de uma agenda que já passaram 
        for agenda in queryset:
            if agenda.dia == datetime.now().date():
                for passado in agenda.horarios.all():
                    if passado.horario.strftime('%H:%M') < datetime.now().strftime('%H:%M'):
                        raise Exception(f'{datetime.today().hour}:{datetime.today().minute}')
                        agenda.horarios.remove(passado.id)

        # Horários que foram preenchidos devem ser excluídos da listagem(ao
        # cadastrar consulta o horario esta sendo removido da agenda
        # assim removendo da listagem)
# queryset
        #  Agendas que todos os seus horários já foram preenchidos devem 
        # ser excluídas da listagem
        queryset = queryset.exclude(horarios=None)
            
        # Ordenado por ordem crecente 
        queryset = queryset.order_by('dia')

        # Agendas para datas passadas devem ser excluídas 
        # da listagem
        queryset = queryset.filter(dia__gte=datetime.now())
        
        return queryset
        


class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, )
    permission_classes = (IsAuthenticated, )
    filter_class = AgendaFilter
    filter_backends = (DjangoFilterBackend, )
    # filterset_fields = ['medico', ]



    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        queryset = AgendaRegrasdeNegocio().list_rn(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)
        


      