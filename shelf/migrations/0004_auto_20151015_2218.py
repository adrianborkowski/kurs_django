# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_auto_20151015_2006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'authors', 'ordering': ('last_name', 'first_name'), 'verbose_name': 'author'},
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last name'),
        ),
    ]
