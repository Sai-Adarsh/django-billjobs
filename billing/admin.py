from django.contrib import admin
from billing.models import Bill, BillLine

class BillLineInline(admin.TabularInline):
    model = BillLine
    extra = 1

class BillAdmin(admin.ModelAdmin):
    inlines = [BillLineInline]

admin.site.register(Bill, BillAdmin)