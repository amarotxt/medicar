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
                        agenda.horarios.remove(passado)

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


    def get_queryset(self):

        response = super().get_queryset()
        
        queryset = self.filter_queryset(response)

        return AgendaRegrasdeNegocio().list_rn(queryset)

   

      