from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import (
    Post, Category
)


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
        'title',
        'slug',
    )
    prepopulated_fields = {'slug': ('title',)}
    mptt_level_indent = 20


admin.site.register(Category, CategoryAdmin)