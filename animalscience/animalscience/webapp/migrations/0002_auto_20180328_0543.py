# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-28 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(default='none', max_length=30)),
                ('project_author_name', models.CharField(default='none', max_length=30)),
                ('project_year', models.DateField(null=True)),
                ('project_keywords', models.CharField(default='none', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
