from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('label', 'amount', 'date', 'category')  # Change 'name' to 'label'
    search_fields = ('label', 'category')  # Change 'name' to 'label'
    list_filter = ('category', 'date')
    ordering = ('-date',)
    date_hierarchy = 'date'


admin.site.register(Expense, ExpenseAdmin)
