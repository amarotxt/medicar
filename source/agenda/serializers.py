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
      extra_kwargs = {
            'medico': {'view_name': 'accounts', 'lookup_field': 'account_name'},
            'users': {'lookup_field': 'username'}
        }
