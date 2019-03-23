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

    class Meta:
        ordering = ("-date", "-price")

    def __str__(self):
        return f"{self.building} {self.unit}: ${self.price} on {self.date}"

    def price_per_sqft(self):
        return self.price / self.square_feet
