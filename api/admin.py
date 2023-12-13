from django.contrib import admin
from .models import Category, News

admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display = ('title', 'category', 'add_time')

admin.site.register(News)
