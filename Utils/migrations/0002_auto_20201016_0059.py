# Generated by Django 3.1.1 on 2020-10-16 05:59

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Utils', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametros',
            name='value',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
