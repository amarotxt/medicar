from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Consulta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agenda = models.ForeignKey("agenda.Agenda", on_delete=models.CASCADE)
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now=True)
    