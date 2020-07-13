from .models import Consulta
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from agenda.models import Agenda
# from agenda.serializers import AgendaSerializer
from medico.serializers import MedicoSerializer
from django.core.serializers.json import DjangoJSONEncoder


class ConsultaSerializer(ModelSerializer):
   dia = serializers.SerializerMethodField()
   medico = serializers.SerializerMethodField()
   user = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
   )

   class Meta:
      model = Consulta
      fields = ['id','dia','horario', 'data_agendamento', 'medico', 'user', 'agenda']
      
   
   def to_representation(self, obj):
        # get the original representation
        # Removendo agenda da resposta 
        ret = super(ConsultaSerializer, self).to_representation(obj)
        ret.pop('agenda')
        return ret 

   def get_dia(self, obj):
      agenda = Agenda.objects.filter(pk=obj.agenda_id).first()
      return agenda.dia

   def get_medico(self, obj):
      from django.core.serializers import serialize

      agenda = Agenda.objects.filter(pk=obj.agenda_id).first()
      if agenda:
         medico = MedicoSerializer(agenda.medico)
     
      else :
         return None

      return medico.data