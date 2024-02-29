from django.contrib import admin
from .models import Company, CompanyContact

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(CompanyContact)
class CompanyContactAdmin(admin.ModelAdmin):
    pass
