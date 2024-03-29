# Generated by Django 2.1.4 on 2021-05-19 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_exercicios'),
    ]

    operations = [
        migrations.CreateModel(
            name='cidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='perfilaluno',
            name='turmas',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cidades',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.estado'),
        ),
    ]
