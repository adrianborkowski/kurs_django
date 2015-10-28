# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0004_auto_20151015_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedition',
            name='book',
            field=models.ForeignKey(to='shelf.Book', related_name='editions'),
        ),
        migrations.AlterField(
            model_name='bookedition',
            name='isbn',
            field=models.CharField(blank=True, max_length=17),
        ),
    ]
