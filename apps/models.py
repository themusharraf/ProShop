from itertools import product

from django.db import models
from shared.models import BaseIDModel, BaseDateModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from ckeditor.fields import RichTextField
from django.db.models import TextChoices
from shared.models import upload_name


class Category(MPTTModel, BaseIDModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', models.CASCADE, 'children', null=True, blank=True)

    def __str__(self):
        return self.name


class Tags(BaseIDModel, BaseDateModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(BaseIDModel, BaseDateModel):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    specification = RichTextField()
    quantity = models.IntegerField(null=True, blank=True)
    shipping_cost = models.IntegerField()
    tags = models.ForeignKey('apps.Tags', models.CASCADE)
    category = models.ForeignKey('apps.Category', models.CASCADE)
    author = models.ForeignKey('users.User', models.CASCADE)

    def __str__(self):
        return self.title


class ProductImage(BaseIDModel):
    class Type(TextChoices):
        IMAGES = 'images', 'Rasmlar'
        DOCUMENTS = 'documents', 'Dokumentlar'
        VIDEOS = 'videos', 'Videolar'

    image = models.ImageField(upload_to=upload_name)
    product = models.ForeignKey('apps.Product', models.CASCADE)
    type = models.CharField(max_length=15, choices=Type.choices)


class Comment(BaseIDModel, BaseDateModel):
    product = models.ForeignKey('apps.Product', models.CASCADE)
    text = models.TextField(max_length=255)
    star = models.SmallIntegerField(default=0)
    author = models.ForeignKey('users.User', models.CASCADE)

    def __str__(self):
        return self.text
