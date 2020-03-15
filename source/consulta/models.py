from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
# Create your models here.


class Consulta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agenda = models.ForeignKey("agenda.Agenda", on_delete=models.CASCADE)
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now=True)

    @classmethod
    def check_data_hora_passado(cls, data, hora):
        # Regra de negocio
        # Não deve ser possível marcar uma consulta
        #  para um dia e horário passados
        today = datetime.now().date()
        time_now = datetime.now().time()
        # TODO: corrigir texto do error
        if today > data:
           
            raise ValidationError(
                "Não é possível cadastrar consultas para datas passadas.")
        else:
            if time_now > hora:
                raise ValidationError(
                    "Não é possível cadastrar consultas para datas passadas.")
        return

    @classmethod
    def check_usuario_possui_consulta(cls, user, dia, horario):
        # Regra de negocio
        # Não deve ser possível marcar uma consulta se
        #  o usuário já possui uma consulta marcada no
        #  mesmo dia e horário
        # TODO: corrigir texto do error

        consultas_user = Consulta.objects.filter(
            user__pk=user.pk, agenda__dia=dia, horario=horario).exists()
        if consultas_user:
            raise ValidationError("O usuário já possui consulta para esta data.")
        return

    @classmethod
    def check_agenda_ocupada(cls, agenda, horario):
        # Regra de negocio
        # Não deve ser possível marcar uma consulta se
        #  o usuário já possui uma consulta marcada no
        #  mesmo dia e horário
        # TODO: corrigir texto do error
        consulta = Consulta.objects.filter(
            agenda=agenda, horario=horario).exists()
        if consulta:
            raise ValidationError("Este horário já está preenchido.")
        return


    def save(self, **kwargs):
        self.clean()
        return super().save(kwargs)

    def clean(self):
        # raise Exception("aq")
        self.check_data_hora_passado(self.agenda.dia, self.horario)
        self.check_usuario_possui_consulta(
            self.user, self.agenda.dia, self.horario)
        self.check_agenda_ocupada(self.agenda, self.horario)
