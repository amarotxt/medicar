from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
# Create your models here.


class Consulta(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    agenda = models.ForeignKey("agenda.Agenda", on_delete=models.PROTECT)
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now=True)

    @classmethod
    def check_data_hora_passado(cls, data, hora):
        # Regra de negocio
        # Não deve ser possível marcar uma consulta
        #  para um dia e horário passados
        today = datetime.now().date()
        time_now = datetime.now().time()
       
        if today > data:
           
            raise ValidationError(
                "Não é possível cadastrar consultas para datas passadas.")
       
        if today == data and time_now > hora:
                raise ValidationError(
                    "Não é possível cadastrar consultas para horas passadas.")

    @classmethod
    def check_usuario_possui_consulta(cls, user, dia, horario):
        # Regra de negocio
        # Não deve ser possível marcar uma consulta se
        #  o usuário já possui uma consulta marcada no
        #  mesmo dia e horário
        consultas_user = Consulta.objects.filter(
            user__pk=user.pk, agenda__dia=dia, horario=horario).exists()
        if consultas_user:
            raise ValidationError("O usuário já possui consulta para esta data.")
        return

    @classmethod
    def check_agenda_horario_invalido(cls, agenda, horario):
        # Regra de negocio
        # Não deve ser possível marcar uma consulta se
        #  o usuário já possui uma consulta marcada no
        #  mesmo dia e horário
        if  not agenda.horarios.filter(horario=horario).exists():
            raise ValidationError({"Este horário não existe na agenda do médico"})
 

    def save(self, **kwargs):
        self.clean()
        # raise Exception(self.agenda.horarios.filter(horario=self.horario))
        horario_remove = self.agenda.horarios.filter(horario=self.horario).first()
        self.agenda.horarios.remove(horario_remove)
        self.agenda.save()
        return super().save(kwargs)

    def clean(self):
        self.check_data_hora_passado(self.agenda.dia, self.horario)
        self.check_usuario_possui_consulta(
            self.user, self.agenda.dia, self.horario)
        self.check_agenda_horario_invalido(self.agenda, self.horario)

