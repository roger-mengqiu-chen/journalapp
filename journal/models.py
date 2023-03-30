from django.db import models
from django.contrib import admin


class Event(models.Model):
    date = models.DateField(null=False, blank=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=True, blank=True, default=None)
    location = models.CharField(null=True, blank=True, default=None, max_length=255)
    category = models.ForeignKey("Category", default=None, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    @admin.display(description="Date")
    def get_event_date(self):
        return self.date.strftime("%Y-%m-%d")

    @admin.display(description="Description")
    def get_event_description(self):
        return self.description

    @admin.display(description="Location")
    def get_event_location(self):
        return self.location

    @admin.display(description="People")
    def get_event_people(self):
        person_ids = list(PersonEvent.objects.filter(event=self).values_list("person_id", flat=True))
        people = list(Person.objects.filter(id__in=person_ids))
        return people

    def get_event_category(self):
        return self.category


class Person(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    sex = models.CharField(null=False, blank=False, max_length=10)
    phone_number = models.CharField(null=True, blank=True, max_length=50)
    address = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.name

    @admin.display(description="Sex")
    def get_person_sex(self):
        return self.sex


class PersonEvent(models.Model):
    person = models.ForeignKey(Person, null=False, blank=False, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=False, blank=False, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
