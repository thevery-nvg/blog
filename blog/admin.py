from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from .forms import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'category', 'created_at', 'get_photo']
    readonly_fields = ['views']
    save_on_top = True
    save_as = True
    list_filter = ['category', 'tags']

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return "no photo"

    get_photo.short_description = 'Фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['id', 'title', 'slug']
    list_display_links = ['title', 'slug']
    search_fields = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['id', 'title', 'slug']
    list_display_links = ['title', 'slug']
    search_fields = ('title',)
