from agenda.models import Agenda
from rest_framework.serializers import ModelSerializer
from medico.serializers import MedicoSerializer


class AgendaSerializer(ModelSerializer):
   medico = MedicoSerializer()
   class Meta:
      model = Agenda
      fields = [
         'id',
         'dia',
         'horarios',
         'medico'
      ]
      