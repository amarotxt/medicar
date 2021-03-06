# Generated by Django 3.0.3 on 2020-06-03 13:48

import agenda.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(validators=[agenda.models.dia_passado])),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.Medico')),
            ],
            options={
                'unique_together': {('medico', 'dia')},
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='agenda.Agenda')),
            ],
        ),
    ]
