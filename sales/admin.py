from django.contrib import admin
from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        "unit",
        "building",
        "date",
        "pretty_price",
        "pretty_square_feet",
        "pretty_price_per_sqft"
    )
    date_hierarchy = "date"
    list_filter = ("building__region", "building")
