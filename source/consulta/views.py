from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from consulta.models import Consulta
from consulta.serializers import ConsultaSerializer
from agenda.models import Agenda

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

        date_now = datetime.now().date()
        queryset = self.filter_queryset(self.get_queryset()).filter(
            agenda__dia__gte=date_now).order_by('-data_agendamento', 'horario')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super().create(request)

    @classmethod
    def check_consulta_aconteceu(cls, consulta):
        # Regra de negocio:
        #   Não deve ser possível desmarcar uma consulta que já aconteceu
        today = datetime.now().date()
        hour = datetime.now().time()
        if today > consulta.agenda.dia:
            raise ValidationError("Esta consulta já aconteceu")
        elif today == consulta.agenda.dia and hour > consulta.horario:
            raise ValidationError("Esta consulta já aconteceu")
        return

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        # Regra de negocio:
        #  Não deve ser possível desmarcar uma consulta que
        # não foi marcada pelo usuário logado
        if not instance:
            raise ValidationError("Esta consulta não existe.")

        check_consulta_aconteceu(instance)

        if request.user.is_staff or request.user == instance.user:
            self.perform_destroy(instance)
        else:
            raise ValidationError("""O usuário não possui permissão 
                para deletar esta consulta.
                Esta consulta já aconteceu.""")

        return super().delete(request)
