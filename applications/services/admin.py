from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'content', 'is_active', )
