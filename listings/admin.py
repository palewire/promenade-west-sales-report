from django.contrib import admin
from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "unit",
        "pretty_price",
        "pretty_square_feet",
        "pretty_price_per_sqft",
        "created",
    )
