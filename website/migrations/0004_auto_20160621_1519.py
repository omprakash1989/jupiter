# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20160621_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='action_url',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
