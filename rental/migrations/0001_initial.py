# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0004_auto_20151015_2218'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('when', models.DateTimeField(default=django.utils.timezone.now)),
                ('returned', models.DateTimeField(blank=True, null=True)),
                ('what', models.ForeignKey(to='shelf.BookItem')),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
