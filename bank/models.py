from django.contrib import admin
from django.db import models


class Transaction(models.Model):
    transaction_date = models.DateField(null=False, blank=False)
    merchant = models.CharField(null=False, blank=False, max_length=255)
    debit = models.DecimalField(null=True, blank=True, default=None, max_digits=10, decimal_places=2)
    credit = models.DecimalField(null=True, blank=True, default=None,max_digits=10, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, default=None, null=True, blank=True)

    def __str__(self):
        return self.merchant

    @admin.display(description="Date")
    def get_transaction_date(self):
        return self.transaction_date.strftime("%Y-%m-%d")

    @admin.display(description="Merchant")
    def get_transaction_merchant(self):
        return self.merchant

    @admin.display(description="Debit")
    def get_transaction_debit(self):
        return self.debit

    @admin.display(description="Credit")
    def get_transaction_credit(self):
        return self.credit

    @admin.display(description="Category")
    def get_transaction_category(self):
        if self.category:
            return self.category.name
        return None


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
