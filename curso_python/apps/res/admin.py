
from django.contrib import admin

from .models import Canton, Partner


@admin.register(Canton)
class CantonAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


@admin.register(Partner)
class ResPartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'identification_type', 'email', 'canton']
    list_filter = ['identification_type', 'activo', 'canton']
    search_fields = ['name', 'last_name', 'email', 'canton__name']