from django.db import models
from django.contrib import admin


class Event(models.Model):
    date = models.DateField(null=False, blank=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=True, blank=True, default=None)
    location = models.CharField(null=True, blank=True, default=None, max_length=255)
    category = models.ForeignKey("Category", default=None, on_delete=models.PROTECT)
    people = models.ManyToManyField("Person")

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
        return ', '.join([a.name for a in self.people.all()])

    def get_event_category(self):
        return self.category


class Person(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    sex = models.CharField(null=False, blank=False, max_length=10)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.name

    @admin.display(description="Sex")
    def get_person_sex(self):
        return self.sex


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
