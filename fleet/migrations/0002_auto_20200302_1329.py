#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 11:16:40
# Last Modified time: Tue 16 June 2020 12:04:46 

# Description:# Generated by Django 3.0.3 on 2020-03-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='html_template',
        ),
        migrations.AddField(
            model_name='campaign',
            name='photo1',
            field=models.FileField(blank=True, null=True, upload_to='campaigns/actions/'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='photo10',
            field=models.FileField(blank=True, null=True, upload_to='campaigns/actions/'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='photo20',
            field=models.FileField(blank=True, null=True, upload_to='campaigns/actions/'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='photo30',
            field=models.FileField(blank=True, null=True, upload_to='campaigns/actions/'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='photo5',
            field=models.FileField(blank=True, null=True, upload_to='campaigns/actions/'),
        ),
    ]
