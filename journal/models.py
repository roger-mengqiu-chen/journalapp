from django.db import models
from django.contrib import admin


class Person(models.Model):
    nick_name = models.CharField(null=False, blank=False, max_length=255)
    first_name = models.CharField(null=False, blank=False, max_length=255)
    last_name = models.CharField(null=True, blank=True, max_length=255)
    sex = models.CharField(null=False, blank=False, max_length=10)
    phone_number = models.CharField(null=True, blank=True, max_length=50)
    address = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return f"{self.first_name} {self.last_name if self.last_name else ''}"


class Event(models.Model):
    date = models.DateField(null=False, blank=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=True, blank=True, default=None)
    location = models.CharField(null=True, blank=True, default=None, max_length=255)
    category = models.ForeignKey("Category", null=True, blank=True, default=None, on_delete=models.SET_DEFAULT)
    people = models.ManyToManyField(Person)

    def __str__(self):
        return self.name

    @admin.display(description="Date")
    def get_event_date(self):
        return self.date.strftime("%Y-%m-%d")

    @admin.display(description="People")
    def get_people(self):
        return ", ".join([person.name for person in list(self.people.all())])


class PersonEvent(models.Model):
    person = models.ForeignKey(Person, null=False, blank=False, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=False, blank=False, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
