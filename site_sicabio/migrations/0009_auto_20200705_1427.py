# Generated by Django 2.0.5 on 2020-07-05 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_sicabio', '0008_auto_20200705_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='dt_nascimento',
            field=models.DateField(),
        ),
    ]
