from especialidade.models import Especialidade
from rest_framework.serializers import ModelSerializer

class EspecialidadeSerializer(ModelSerializer):
     class Meta:
        model = Especialidade
        fields = '__all__'