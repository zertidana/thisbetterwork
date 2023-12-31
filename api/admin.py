from django.contrib import admin
from .models import Category, News, Comment, Profile

admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    # It isn't showing the time for some reason; fix it 
    list_display = ('title', 'category', 'add_time', 'preview')

admin.site.register(News, AdminNews)

class AdminComment(admin.ModelAdmin):
    list_display = ('news', 'email', 'comment', 'status')

admin.site.register(Comment, AdminComment)
admin.site.register(Profile)


