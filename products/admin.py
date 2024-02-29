from django.contrib import admin
from .models import Price, Discount, DiscountScale, Product

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass

@admin.register(DiscountScale)
class DiscountScaleAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
