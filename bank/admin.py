from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from bank.models import Transaction, Category


class TransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("get_transaction_date",
                    "merchant",
                    "debit",
                    "credit",
                    "category",
                    "action")
    list_display_links = ("merchant",)
    search_fields = ["merchant"]
    autocomplete_fields = ["category"]
    list_per_page = 15

    list_editable = ["category"]

    def action(self, obj):
        return format_html('<a class="btn" href="/admin/bank/transaction/{}/delete/">Delete</a>', obj.id)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["category"]


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)
