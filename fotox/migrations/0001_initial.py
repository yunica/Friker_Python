# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_created=True)),
                ('nombre', models.CharField(blank='', max_length=15, null=True)),
                ('apellido', models.CharField(blank='', max_length=15, null=True)),
            ],
        ),
    ]