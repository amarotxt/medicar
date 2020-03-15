from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField

def dia_passado(value):
    if datetime.now().date() > value:
        raise ValidationError('Não é possivel criar uma agenda com a data passada.')

# Create your models here.
class Agenda(models.Model):
    medico = models.ForeignKey('medico.Medico', on_delete=models.CASCADE)
    dia = models.DateField(validators=[dia_passado])
    horarios = ArrayField(models.TimeField())
     
    def save(self, **kwargs):
        self.clean()
        return super().save(kwargs)
        
    def clean(self):
        agenda_dia = Agenda.objects.filter(dia=self.dia, medico=self.medico)
        if agenda_dia.exists():
            raise ValidationError ("Este medico ja possui agenda para este dia.")   
        return super().clean()