from django.contrib import admin
from .models import Main


@admin.register(Main)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'created_at')
    list_display_links = ('id', 'name', 'author')
    search_fields = ('id', 'name')
