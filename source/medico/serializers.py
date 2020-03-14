from agenda.models import Agenda
from rest_framework.serializers import ModelSerializer

class MedicoSerializer(ModelSerializer):
     class Meta:
        model = Agenda
        fields = '__all__'