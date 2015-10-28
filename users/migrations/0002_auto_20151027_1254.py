# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bibliouser',
            name='avatar',
            field=models.ImageField(upload_to='avatars/', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bibliouser',
            name='phone',
            field=models.CharField(max_length=15, default='', blank=True),
        ),
    ]
