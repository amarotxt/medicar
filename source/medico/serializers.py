from medico.models import Medico
from rest_framework.serializers import ModelSerializer

class MedicoSerializer(ModelSerializer):
     class Meta:
        model = Medico
        fields = '__all__'