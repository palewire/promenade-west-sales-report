from django.contrib import admin
from .models import Pending


@admin.register(Pending)
class PendingAdmin(admin.ModelAdmin):
    list_display = (
        "unit",
        "pretty_price",
        "pretty_square_feet",
        "pretty_price_per_sqft",
        "created",
    )
