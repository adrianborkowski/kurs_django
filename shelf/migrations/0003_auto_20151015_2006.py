# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20151014_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookEdition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('isbn', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('catalogue_number', models.CharField(max_length=30)),
                ('cover_type', models.CharField(max_length=4, choices=[('soft', 'Soft'), ('hard', 'Hard')])),
                ('edition', models.ForeignKey(to='shelf.BookEdition')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='shelf.Author'),
        ),
        migrations.AddField(
            model_name='bookedition',
            name='book',
            field=models.ForeignKey(to='shelf.Book'),
        ),
        migrations.AddField(
            model_name='bookedition',
            name='publisher',
            field=models.ForeignKey(to='shelf.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='shelf.BookCategory'),
        ),
    ]
