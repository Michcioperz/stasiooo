from django.contrib import admin
from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'publication_time', 'approved', 'pinned',)
