# Generated by Django 3.2.9 on 2021-12-03 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=8)),
                ('equipo', models.CharField(max_length=9)),
                ('comentario', models.TextField(max_length=100)),
                ('ipequipo', models.CharField(max_length=64)),
                ('salon', models.CharField(max_length=9)),
            ],
        ),
    ]
