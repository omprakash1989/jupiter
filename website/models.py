from django.db import models, IntegrityError
from django.utils.text import slugify
from django.contrib.auth.models import User

import binascii
import os, requests, json, datetime
from jupiter.settings import logger
import uuid
from django.core.exceptions import ObjectDoesNotExist, ValidationError


class Banners(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image_url = models.ImageField(upload_to='banners/slider/')
    action_url = models.CharField(max_length=255, blank=True)
    priority = models.IntegerField(null=True, default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(db_index=True, default=True)
    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    display_name = models.CharField(max_length=100, blank=False)
    action_url = models.CharField(max_length=255, blank=True)
    banner_image = models.ImageField(upload_to='banners/category/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    is_active = models.BooleanField(db_index=True, default=True)

    def __unicode__(self):
        return self.display_name


class Products(models.Model):
    name = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    image_url = models.ImageField(upload_to='product/')
    price_effective = models.FloatField(default=1)
    price_marked = models.FloatField(default=1)
    product_info = models.TextField(blank=True)
    product_description = models.TextField(blank=True)
    discount = models.FloatField(default=0)
    priority = models.IntegerField(null=True, default=0)
    updated_on = models.DateTimeField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(db_index=True, default=True)
    category = models.ForeignKey(Category, null=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()

    def __unicode__(self):
        return self.name


class ProductImages(models.Model):
    image_url = models.ImageField(upload_to='product_images/')
    product_id = models.ForeignKey(Products, db_index=True, null=True)


class HomePageSegments(models.Model):
    category = models.ForeignKey(Category, null=True, unique=True)

    def __unicode__(self):
        return self.category.display_name