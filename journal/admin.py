from django.contrib import admin

from journal.models import Event, Person, Category, PersonEvent


class PersonEventInlineFormset(admin.TabularInline):
    model = PersonEvent
    extra = 0
    autocomplete_fields = ["person"]


class EventAdmin(admin.ModelAdmin):
    search_fields = ["people__name"]
    autocomplete_fields = ["people"]
    list_display = ('get_event_date', 'name', 'get_event_description', 'get_event_location', 'get_event_people')
    inlines = [PersonEventInlineFormset]


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_person_sex')
    search_fields = ["name"]


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Category, CategoryAdmin)
