from datetime import datetime
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from agenda.models import Agenda
from agenda.serializers import AgendaSerializer
from .filters import DateFilter
from consulta.models import Consulta
# Create your views here.


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filter_class = DateFilter
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['medico', 'especialidade']

    def list(self, request):
        date_now =  datetime.now().date()
        time_now = datetime.now().time()
        queryset = self.filter_queryset(self.get_queryset()).filter(dia__gte=date_now).order_by('-dia','horarios')
        consultas = Consultas.objects.all()
        raise Exception(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
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
