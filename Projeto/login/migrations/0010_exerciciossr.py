# Generated by Django 2.1.4 on 2021-05-20 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20210519_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='exerciciossr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('enunciado', models.CharField(max_length=99999)),
                ('resposta', models.CharField(max_length=99999)),
                ('materia', models.IntegerField()),
            ],
        ),
    ]
