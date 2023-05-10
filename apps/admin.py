from django.contrib import admin
from django.utils.html import format_html

from apps.models import Category, Product, ProductImage, Tags
from mptt.admin import DraggableMPTTAdmin


class ProductStackedInline(admin.StackedInline):
    model = Product
    min_num = 0
    extra = 2
    max_num = 2


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    search_fields = ('name',)
    inlines = (ProductStackedInline,)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    fields = ('image',)
    min_num = 1
    extra = 1
    max_num = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
    list_filter = ['price']
    search_fields = ('title', 'description')
    inlines = [ProductImageInline]



@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
