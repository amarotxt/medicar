from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField

def dia_passado(value):
    if datetime.now().date() > value:
        raise ValidationError('Não é possivel criar uma agenda com a data passada.')

class Horario(models.Model):
    horario = models.TimeField() 
   
    def __str__(self):     
        return  self.horario.strftime('%H:%M')

# Create your models here.
class Agenda(models.Model):
    medico = models.ForeignKey('medico.Medico', on_delete=models.CASCADE)
    dia = models.DateField(validators=[dia_passado])
    horarios = models.ManyToManyField(
        "Horario", verbose_name=("Horarios Disponiveis"))
    
    class Meta:
        unique_together = ('medico', 'dia')

    def save(self, **kwargs):
        self.clean()
        return super().save(kwargs)
    
    def __str__(self):
        return f"{self.medico.nome} - data: {self.dia}"
