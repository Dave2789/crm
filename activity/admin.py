from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_id', 'company', 'user', 'type_activity', 'campaign', 'description', 'activity_date', 'activity_hour', 'end_date', 'finish', 'process', 'status', 'document')
    search_fields = ['description']