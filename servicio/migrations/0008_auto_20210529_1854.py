# Generated by Django 3.1.6 on 2021-05-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0007_auto_20210528_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='num_telf',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tracking',
            field=models.BigIntegerField(),
        ),
    ]