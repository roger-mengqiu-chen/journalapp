from django.contrib import admin
from django.db import models


class Transaction(models.Model):
    transaction_date = models.DateField(null=False, blank=False)
    merchant = models.CharField(null=False, blank=False, max_length=255)
    debit = models.DecimalField(null=False, blank=False, default=0.0, max_digits=10, decimal_places=2)
    credit = models.DecimalField(null=False, blank=False, default=0.0,max_digits=10, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, default=None, null=True, blank=True)

    def __str__(self):
        return self.merchant

    @admin.display(description="Date")
    def get_transaction_date(self):
        return self.transaction_date.strftime("%Y-%m-%d")

    @admin.display(description="Category")
    def get_transaction_category(self):
        if self.category:
            return self.category.name
        return None


class Category(models.Model):
    types = ["EXPENSE", "INCOME"]

    name = models.CharField(null=False, blank=False, max_length=255, unique=True)
    type = models.CharField(max_length=10, choices=[(x, x) for x in types], default="EXPENSE")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
