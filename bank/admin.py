from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from bank.models import Transaction, Category
from django.contrib.admin.views.main import ChangeList


class TransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("get_transaction_date",
                    "merchant",
                    "debit",
                    "credit",
                    "category")
    list_display_links = ("merchant",)
    search_fields = ["merchant"]
    list_per_page = 15

    list_editable = ["category"]


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)
