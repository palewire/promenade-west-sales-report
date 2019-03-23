from django.contrib import admin
from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("unit", "building",  "date",  "price")
    date_hierachy = ("date",)
