from django.contrib import admin
from apps.models import Category, Product, ProductImage, Tags
from mptt.admin import DraggableMPTTAdmin

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    ...


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    fields = ('image',)
    min_num = 1
    extra = 1
    max_num = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    ...
