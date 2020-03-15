from .models import Consulta
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from agenda.models import Agenda

class ConsultaSerializer(ModelSerializer):
   dia = serializers.SerializerMethodField()
   medico = serializers.SerializerMethodField()

   class Meta:
      model = Consulta
      fields = ['id', 'horario', 'data_agendamento']

   def get_dia(self, obj):
      agenda = Agenda.objects.filter(pk=self.agenda.pk).first()
      return agenda.dia

   def get_medico(self, obj):
      agenda = Agenda.objects.filter(pk=self.agenda.pk).first()
      return agenda.medico