from django.contrib import admin
from .models import Company, Person


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['created_at']
    ordering = ['name']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'position', 'company', 'hire_date']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['company', 'position', 'hire_date', 'created_at']
    autocomplete_fields = ['company']
    ordering = ['last_name', 'first_name']
    list_select_related = ['company']