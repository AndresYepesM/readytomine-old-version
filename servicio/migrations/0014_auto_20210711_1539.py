# Generated by Django 3.1 on 2021-07-11 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0013_auto_20210709_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='estado',
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]