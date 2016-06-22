# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20160622_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='homepagesegments',
            name='category_id',
        ),
        migrations.AddField(
            model_name='homepagesegments',
            name='category',
            field=models.ForeignKey(null=True, to='website.Category', unique=True),
        ),
    ]
