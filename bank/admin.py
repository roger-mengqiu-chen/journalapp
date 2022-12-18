from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from bank.models import Transaction, Category
from django.contrib.admin.views.main import ChangeList


# Register your models here.
class TransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("get_transaction_date",
                    "get_transaction_merchant",
                    "get_transaction_debit",
                    "get_transaction_credit",
                    "get_transaction_category")
    list_display_links = ("get_transaction_merchant",)




class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)
