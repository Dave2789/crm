from django.contrib import admin
from .models import CampaignType, CompanyPhase, CompanySize, CompanyType, Currency, InvoiceUse, PaymentCondition, PaymentMethod, ProductCategory, Status, Country, State, City, Business, Platform, Rol, SubTypeActivity, TypeActivity, WayToPay

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_id', 'description', 'module', 'created_at', 'update_at')
    search_fields = ['description']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['country_name']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('state_id', 'country_id', 'state_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['state_name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'state_id', 'city_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['city_name']

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('business_id', 'business_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['business_name', 'business_id']

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('platform_id', 'platform_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['platform_name']

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('rol_id', 'rol_name', 'permissions', 'status_id', 'created_at', 'update_at')
    search_fields = ['rol_name']

@admin.register(CampaignType)
class CampaignTypeAdmin(admin.ModelAdmin):
    list_display = ('campaign_type_id', 'campaign_type_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['campaign_type_name']

@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ('company_type_id', 'type_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['type_name']

@admin.register(CompanySize)
class CompanySizeAdmin(admin.ModelAdmin):
    list_display = ('company_size_id', 'size_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['size_name']

@admin.register(CompanyPhase)
class CompanyPhaseAdmin(admin.ModelAdmin):
    list_display = ('company_phase_id', 'phase_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['phase_name']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product_category_id', 'category_name', 'description', 'status_id', 'created_at', 'update_at')
    search_fields = ['category_name']

@admin.register(TypeActivity)
class TypeActivityAdmin(admin.ModelAdmin):
    list_display = ('type_activity_id', 'activity', 'icon', 'color', 'status_id', 'created_at', 'update_at')
    search_fields = ['activity']

@admin.register(SubTypeActivity)
class SubTypeActivityAdmin(admin.ModelAdmin):
    list_display = ('sub_type_activity_id', 'type_activity', 'sub_activity', 'color', 'status_id', 'created_at', 'update_at')
    search_fields = ['sub_activity']

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_id', 'currency_name', 'currency_abrev', 'status_id', 'created_at', 'update_at')
    search_fields = ['currency_name']

@admin.register(WayToPay)
class WayToPayAdmin(admin.ModelAdmin):
    list_display = ('way_to_pay_id', 'way_to_pay_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['way_to_pay_name']

@admin.register(PaymentCondition)
class PaymentConditionAdmin(admin.ModelAdmin):
    list_display = ('payment_condition_id', 'payment_condition_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['payment_condition_name']

@admin.register(InvoiceUse)
class InvoiceUseAdmin(admin.ModelAdmin):
    list_display = ('invoice_use_id', 'invoice_use_code', 'invoice_use_name', 'status_id', 'created_at', 'update_at')
    search_fields = ['invoice_use_name']