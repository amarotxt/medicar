from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField

def dia_passado(value):
    if datetime.now() >= value:
        raise ValidationError('Não é possivel criar uma agenda com a data passada.')

# Create your models here.
class Agenda(models.Model):
    medico = models.ForeignKey('medico.Medico', on_delete=models.CASCADE)
    dia = models.DateField(validators=[dia_passado])
    horarios = ArrayField(models.TimeField())