# Generated by Django 2.0.5 on 2020-07-20 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_sicabio', '0003_auto_20200719_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='horario',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dt_nascimento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
