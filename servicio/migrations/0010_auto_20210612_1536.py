# Generated by Django 3.1.6 on 2021-06-12 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0009_auto_20210612_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partes',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Partes por arreglar'},
        ),
    ]