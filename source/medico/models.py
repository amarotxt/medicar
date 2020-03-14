from django.db import models


class Medico(models.Model):
    nome = models.CharField(max_length=120)
    crm = models.CharField(max_length=40)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    especialidade = models.ForeignKey(
        'especialidade.Especialidade',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name