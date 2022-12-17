from django.contrib import admin

from journal.models import Event, Person


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Person, PersonAdmin)
