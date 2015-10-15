# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
