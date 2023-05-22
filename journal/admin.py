from django.contrib import admin
from django.utils.html import format_html

from journal.models import Event, Person, Category, PersonEvent


class PersonEventInlineFormset(admin.TabularInline):
    model = PersonEvent
    extra = 0
    autocomplete_fields = ["person"]


class EventAdmin(admin.ModelAdmin):
    autocomplete_fields = ["people", "category"]
    list_display = ('get_event_date', 'name', 'description', 'location', 'get_people', 'action')
    inlines = [PersonEventInlineFormset]

    def action(self, obj):
        return format_html('<a class="btn" href="/admin/journal/event/{}/delete/">Delete</a>', obj.id)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('nick_name', 'sex')
    search_fields = ["name"]


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Event, EventAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Category, CategoryAdmin)
