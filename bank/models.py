from django.db import models


class Transaction(models.Model):
    transaction_date = models.DateField(null=False, blank=False)
    merchant = models.CharField(null=False, blank=False, max_length=255)
    debit = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    credit = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, default=None)


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
