# Generated by Django 2.0.5 on 2020-06-27 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_sicabio', '0013_auto_20200627_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='paciente_id',
            new_name='paciente',
        ),
        migrations.RenameField(
            model_name='consulta',
            old_name='profissional_id',
            new_name='profissional',
        ),
    ]
