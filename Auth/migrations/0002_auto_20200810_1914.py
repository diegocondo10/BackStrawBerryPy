# Generated by Django 3.1 on 2020-08-11 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='first_name',
            field=models.CharField(default='NO REGISTRA', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(default='NO REGISTRA', max_length=150, null=True),
        ),
    ]
