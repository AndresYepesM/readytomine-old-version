# Generated by Django 3.1.6 on 2021-06-12 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0008_auto_20210612_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partes',
            name='proceso',
        ),
        migrations.DeleteModel(
            name='ParteProceso',
        ),
    ]
