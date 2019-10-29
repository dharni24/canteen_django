# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.IntegerField()),
                ('roll', models.CharField(max_length=15)),
                ('desc', models.CharField(max_length=100)),
                ('total', models.IntegerField()),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll', models.CharField(max_length=15)),
                ('psw', models.CharField(max_length=20)),
                ('wallet', models.IntegerField()),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
