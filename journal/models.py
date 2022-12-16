from django.db import models


class Event(models.Model):
    date = models.DateField(null=False, blank=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=True, blank=True, default=None)
    location = models.CharField(null=True, blank=True, default=None, max_length=255)
    category = models.CharField(null=False, blank=False, default="Life", max_length=255)


class Person(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    sex = models.CharField(null=False, blank=False, max_length=10)


class PersonEvent(models.Model):
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)

