from django.db import models
from buildings.models import Building


class Sale(models.Model):
    """
    The sale of a unit in a building.
    """
    # About the unit
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    url = models.CharField(max_length=2000, unique=True)
    unit = models.CharField(max_length=100)
    square_feet = models.IntegerField()
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)

    # About the sale
    price = models.FloatField()
    date = models.DateField()

    # About our scrape
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date", "-price")

    def __str__(self):
        return f"{self.building.name} {self.unit}: {self.pretty_price} on {self.date}"

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
        return f"${self.price / self.square_feet:,.0f}"
    # pretty_price_per_sqft.short_description = "price per square foot"
