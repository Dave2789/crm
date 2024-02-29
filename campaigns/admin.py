from django.contrib import admin
from .models import Campaign, CampaignUser, CampaignCompany

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('campaign_id', 'campaign_code', 'campaign_name', 'amount_invested', 'start_date', 'start_date')
    search_fields = ['campaign_name']

@admin.register(CampaignUser)
class CampaignUserAdmin(admin.ModelAdmin):
    list_display = ('campaign_user_id', 'user', 'status_id', 'created_at', 'update_at')
    search_fields = ['user']

@admin.register(CampaignCompany)
class CampaignCompanyAdmin(admin.ModelAdmin):
    list_display = ('campaign_company_id', 'company', 'total_quote', 'total_sale', 'status_id', 'created_at', 'update_at')
    search_fields = ['company']