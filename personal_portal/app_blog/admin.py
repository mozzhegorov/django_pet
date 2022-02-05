from django.contrib import admin
from app_blog.models import BlogEntryModel


class BlogEntryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created',
    )


admin.register(BlogEntryModel, BlogEntryAdmin)
