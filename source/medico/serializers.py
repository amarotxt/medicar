from medico.models import Medico
from rest_framework.serializers import ModelSerializer
from especialidade.serializers import EspecialidadeSerializer
class MedicoSerializer(ModelSerializer):
   especialidade = EspecialidadeSerializer()
   class Meta:
      model = Medico
      fields = ['id', 'crm', 'nome','especialidade']