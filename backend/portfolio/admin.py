from django.contrib import admin
from .models import Application, Tattoo

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Tattoo)
class TattooAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)