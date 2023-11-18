from django.contrib import admin

from product.models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'color',
        'weight',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'color',
        'created_at'
    )

    date_hierarchy = 'created_at'