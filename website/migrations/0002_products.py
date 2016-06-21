# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('image_url', models.ImageField(upload_to=b'banners/slider/')),
                ('action_url', models.CharField(max_length=255, blank=True)),
                ('priority', models.IntegerField(default=True, null=True)),
                ('updated_on', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, db_index=True)),
            ],
        ),
    ]
