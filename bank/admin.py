from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from bank.models import Transaction, Category


class TransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("transaction_date",
                    "merchant",
                    "debit",
                    "credit",
                    "category",
                    "action")
    list_display_links = ("merchant",)
    search_fields = ["merchant"]
    autocomplete_fields = ["category"]
    list_per_page = 15
    list_filter = ["category"]
    list_editable = ["category"]
    sortable_by = ["transaction_date", "merchant", "debit", "credit", "category"]

    def action(self, obj):
        return format_html('<a class="btn" href="/admin/bank/transaction/{}/delete/">Delete</a>', obj.id)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ("name", "type")
    list_filter = ["type"]
    sortable_by = ["name"]


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)
