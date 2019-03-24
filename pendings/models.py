from django.db import models
from .managers import PendingManager


class Pending(models.Model):
    """
    The pending sale of a unit in Promenade West.
    """
    # About the unit
    url = models.CharField(max_length=2000, unique=True)
    unit = models.CharField(max_length=100)
    square_feet = models.IntegerField()
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)

    # About the listing
    date = models.DateField()
    price = models.FloatField()

    # About our scrape
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Managers
    objects = PendingManager()

    class Meta:
        ordering = ("-price",)

    def __str__(self):
        return f"{self.unit or 'Unknown'} for {self.pretty_price()}"

    def pretty_price(self):
        return f"${self.price:,.0f}"
    pretty_price.short_description = "price"
    pretty_price.admin_order_field = "price"

    def pretty_square_feet(self):
        return f"{self.square_feet:,.0f}"
    pretty_square_feet.short_description = "square feet"
    pretty_square_feet.admin_order_field = "square_feet"

    def price_per_sqft(self):
        return self.price / self.square_feet

    def pretty_price_per_sqft(self):
        return f"${self.price_per_sqft():,.0f}"
    pretty_price_per_sqft.short_description = "price per square foot"
