# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20160621_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageSegments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_id', models.ForeignKey(to='website.Category', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='priority',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
