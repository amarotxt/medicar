from agenda.models import Agenda
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from medico.serializers import MedicoSerializer
from .models import Horario

class AgendaSerializer(ModelSerializer):
   # medico = MedicoSerializer()
   horarios = serializers.StringRelatedField(
        many=True)
     
   class Meta:
      model = Agenda
      fields = [
         'id',
         'medico',
         'dia',
         'horarios'
      ]

   # def get_horario(self, obj):
   #    horario_query = Horario.objects.filter(agenda=obj)
   #    raise Exception("aq")
   #    return list(horario_query)
      