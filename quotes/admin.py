from django.contrib import admin
from .models import Quote, QuoteOption, OptionProduct

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    pass

@admin.register(QuoteOption)
class QuoteOptionAdmin(admin.ModelAdmin):
    pass

@admin.register(OptionProduct)
class OptionProductAdmin(admin.ModelAdmin):
    pass