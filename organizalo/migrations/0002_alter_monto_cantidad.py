# Generated by Django 4.0.5 on 2022-06-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizalo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monto',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]
