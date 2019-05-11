# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-11 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kimita', '0005_auto_20190512_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(to='kimita.languages'),
        ),
    ]
