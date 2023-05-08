from django.contrib import admin
from apps.models import Category, Product, ProductImage, Tags


@admin.register(Category)
class CategoryAdmin(admin.Admin):
    ...


@admin.register(Product)
class ProductAdmin(admin.Admin):
    ...


@admin.register(ProductImage)
class ProductImageAdmin(admin.Admin):
    ...


@admin.register(Tags)
class TagsAdmin(admin.Admin):
    ...
