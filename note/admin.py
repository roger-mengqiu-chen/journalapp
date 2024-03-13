from django.contrib import admin

from note.models import Note, Tag, Category

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ["title"]
    list_filter = ['created_at', 'updated_at']

admin.site.register(Note, NoteAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ["name"]

admin.site.register(Tag, TagAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ["name"]

admin.site.register(Category, CategoryAdmin)
