# Generated by Django 2.1.4 on 2021-05-20 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20210518_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicioss',
            name='materia',
            field=models.IntegerField(),
        ),
    ]
