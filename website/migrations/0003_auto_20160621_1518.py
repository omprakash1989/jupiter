# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('display_name', models.CharField(max_length=100)),
                ('action_url', models.CharField(max_length=255)),
                ('banner_image', models.ImageField(upload_to=b'banners/category/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('is_active', models.BooleanField(default=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_url', models.ImageField(upload_to=b'product_images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='action_url',
        ),
        migrations.AddField(
            model_name='products',
            name='discount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='price_effective',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='products',
            name='price_marked',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='products',
            name='image_url',
            field=models.ImageField(upload_to=b'product/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='productimages',
            name='product_id',
            field=models.ForeignKey(to='website.Products', null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='category_id',
            field=models.ForeignKey(to='website.Category', null=True),
        ),
    ]
