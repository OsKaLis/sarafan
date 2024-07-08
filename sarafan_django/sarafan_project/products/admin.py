from django.contrib import admin

from .models import (
    Category, UnderCategory, SizeImage, Products, Basket
)


@admin.register(Category)
class CategoryPanel(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
        'picture',
    )
    list_editable = ('name', 'slug',)


@admin.register(UnderCategory)
class UnderCategoryPanel(admin.ModelAdmin):
    list_display = (
        'pk',
        'category',
        'name',
        'slug',
        'picture',
    )
    list_editable = ('name', 'slug',)
    list_filter = ('category',)


class LogosProductsPanel(admin.TabularInline):
    model = SizeImage


@admin.register(Products)
class ProductsPanel(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
        'price',
        'current_under_category',
    )
    inlines = [LogosProductsPanel]


@admin.register(Basket)
class BasketPanel(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'products',
        'quantity'
    )


@admin.register(SizeImage)
class SizeImagePanel(admin.ModelAdmin):
    list_display = (
        'pk',
        'logo_products',
        'size_1',
        'size_2',
        'size_3'
    )
