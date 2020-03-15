# Generated by Django 3.0.3 on 2020-03-15 03:53

import agenda.models
import django.contrib.postgres.fields
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
                ('horarios', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), size=None)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.Medico')),
            ],
        ),
    ]
