from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from bank.models import Transaction, Category


# Register your models here.
class TransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)
