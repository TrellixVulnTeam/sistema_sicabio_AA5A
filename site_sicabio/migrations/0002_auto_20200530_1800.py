# Generated by Django 2.0.5 on 2020-05-30 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_sicabio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sqtle', models.IntegerField()),
                ('sqtld', models.IntegerField()),
                ('sqtl', models.IntegerField()),
                ('d_dez', models.IntegerField()),
                ('qtd_total_verticilos', models.IntegerField()),
                ('qtd_total_arcos', models.IntegerField()),
                ('qtd_total_presilhas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ImpressaoDigital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.FilePathField(path=None)),
            ],
        ),
        migrations.CreateModel(
            name='MaoDireita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_dedo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MaoEsquerda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_dedo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_paciente', models.CharField(max_length=100)),
                ('cpf_paciente', models.CharField(max_length=12)),
                ('imp_digital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imp_digital', to='site_sicabio.ImpressaoDigital')),
                ('resultado_perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imp_digital', to='site_sicabio.Analise')),
            ],
        ),
        migrations.CreateModel(
            name='Padrao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('padroes', models.CharField(choices=[('W', 'Verticilo'), ('L', 'Presilha'), ('A', 'Arco')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Potencialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('F', 'Força'), ('V', 'Velocidade'), ('CM', 'Coordenação Motora'), ('A', 'Agilidade'), ('R', 'Resistência')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='profissional',
            name='especialidade',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profissional',
            name='user_cpf',
            field=models.CharField(max_length=12),
        ),
        migrations.AddField(
            model_name='maoesquerda',
            name='padrao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mao_esquerda', to='site_sicabio.Padrao'),
        ),
        migrations.AddField(
            model_name='maodireita',
            name='padrao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mao_direita', to='site_sicabio.Padrao'),
        ),
        migrations.AddField(
            model_name='impressaodigital',
            name='mao_direita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='im_digital', to='site_sicabio.MaoDireita'),
        ),
        migrations.AddField(
            model_name='impressaodigital',
            name='mao_esquerda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='im_digital', to='site_sicabio.MaoEsquerda'),
        ),
        migrations.AddField(
            model_name='impressaodigital',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='im_digital', to='site_sicabio.Paciente'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='id_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='site_sicabio.Paciente'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='id_profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='site_sicabio.Profissional'),
        ),
        migrations.AddField(
            model_name='analise',
            name='Resultado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analise', to='site_sicabio.Potencialidade'),
        ),
        migrations.AddField(
            model_name='analise',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='site_sicabio.Paciente'),
        ),
    ]
