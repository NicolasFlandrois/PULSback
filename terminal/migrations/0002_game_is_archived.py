#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 11:16:40
# Last Modified time: Tue 16 June 2020 12:06:07 

# Description:# Generated by Django 3.0.3 on 2020-03-02 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
