from django.contrib import admin
from .models import NewsStory, Comment

# Register your models here.

class NewsStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(NewsStory, NewsStoryAdmin)
admin.site.register(Comment)

