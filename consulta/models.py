from django.db import models

# Create your models here.
class Consulta(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now=True)
    medico = models.ForeignKey('medico.Medico', on_delete=models.PROTECT)