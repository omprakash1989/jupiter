from django.contrib import admin
from website.models import Banners, Products, Category, ProductImages

admin.site.register(Banners)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(ProductImages)
# admin.site.register(Book)