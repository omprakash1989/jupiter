from django.contrib import admin
from website.models import Banners, Products, Category, ProductImages, HomePageSegments

admin.site.register(Banners)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(ProductImages)
admin.site.register(HomePageSegments)
# admin.site.register(Book)