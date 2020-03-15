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


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_class = AgendaFilter
    filter_backends = (DjangoFilterBackend, )
    # filterset_fields = ['medico', ]

    @classmethod
    def clean_list_dates(cls, queryset):
        #Horários dentro de uma agenda que já
        #passaram ou que foram preenchidos 
        # devem ser excluídos da listagem
        time_now = datetime.now().time()
        for agenda in queryset:
            agenda.horarios = [horario for horario in agenda.horarios if horario > time_now]   

        return queryset

    def list(self, request):
        date_now = datetime.now().date()
        queryset = self.clean_list_dates(
            self.filter_queryset(
                self.get_queryset()).filter(
                    dia__gte=date_now).order_by(
                        '-dia', 'horarios'))
        # consultas = Consultas.objects.all()
        # raise Exception(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer=self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer=self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
