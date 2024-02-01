from django.contrib import admin
from .models import Books
# Register your models here.


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'created_at')
    list_display_links = ('id', 'name', 'author')
    search_fields = ('name', 'author')

