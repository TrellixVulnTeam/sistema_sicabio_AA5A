# Generated by Django 3.1 on 2020-08-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_sicabio', '0007_auto_20200721_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impressao',
            name='img_path',
        ),
        migrations.AddField(
            model_name='consulta',
            name='consulta_realizada',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='impressao',
            name='cont',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='impressao',
            name='img',
            field=models.ImageField(blank=True, default='media/avatar.png', null=True, upload_to='impressoes'),
        ),
        migrations.AlterField(
            model_name='impressao',
            name='mao',
            field=models.CharField(choices=[('ME', 'Mão Esquerda'), ('MD', 'Mão Direita')], max_length=2),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cpf_paciente',
            field=models.CharField(default=False, max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='potencialidade',
            name='tipo',
            field=models.CharField(choices=[('F', 'Força'), ('V', 'Velocidade'), ('CM', 'Coordenação Motora'), ('A', 'Agilidade'), ('R', 'Resistência')], max_length=2),
        ),
        migrations.AlterField(
            model_name='resetpassword',
            name='confirmed',
            field=models.BooleanField(blank=True, default=False, verbose_name='Confirmado?'),
        ),
    ]
