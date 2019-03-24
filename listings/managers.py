import statistics
from django.db import models


class ListingQuerySet(models.QuerySet):

    def median_price(self):
        """
        The median sales price.
        """
        values = self.values_list("price", flat=True).order_by("price")
        return statistics.median(values)

    def median_price_per_sqft(self):
        """
        The median sales price divided into the size of the unit.
        """
        inputs = self.values_list("price", "square_feet", named=True)
        values = sorted([t.price / t.square_feet for t in inputs])
        return statistics.median(values)


class ListingManager(models.Manager):

    def get_queryset(self):
        return ListingQuerySet(self.model, using=self._db)

    def median_price(self):
        return self.get_queryset().median_price()

    def median_price_per_sqft(self):
        return self.get_queryset().median_price_per_sqft()
