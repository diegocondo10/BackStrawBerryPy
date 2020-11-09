# Generated by Django 3.1.1 on 2020-10-20 04:46

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Matriculas', '0007_auto_20201017_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodolectivo',
            name='responsables',
        ),
        migrations.AddField(
            model_name='periodolectivo',
            name='responsables',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='alumnoaula',
            table='AlumnoAula',
        ),
        migrations.AlterModelTable(
            name='aula',
            table='Aula',
        ),
        migrations.AlterModelTable(
            name='materia',
            table='Materia',
        ),
        migrations.AlterModelTable(
            name='notamateria',
            table='NotaMateri',
        ),
        migrations.AlterModelTable(
            name='periodolectivo',
            table='PeriodoLectivo',
        ),
        migrations.DeleteModel(
            name='ResponsablePeriodo',
        ),
    ]