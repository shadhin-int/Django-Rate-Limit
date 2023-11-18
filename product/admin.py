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
        'create_at',
        'updated_at',
    )

    list_filter = (
        'color',
        'create_at'
    )

    date_hierarchy = 'create_at'