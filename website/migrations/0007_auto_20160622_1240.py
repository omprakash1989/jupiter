# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20160622_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_info',
            field=models.TextField(blank=True),
        ),
    ]
