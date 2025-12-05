from django.contrib import admin

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('title','price')
    list_filter = ('category',)
    search_fields = ('title','genre')
