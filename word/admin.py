from django.contrib import admin
from .models import Word

@admin.register(Word)
class AdminWord(admin.ModelAdmin):
    list_display = ['id', 'word', 'count', 'created_at']
