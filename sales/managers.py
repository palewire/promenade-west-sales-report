from django.db import models
from django.utils import timezone
from datetime import timedelta


class SaleQuerySet(models.QuerySet):

    def the_last_year(self):
        """
        Sales in the 12 months leading up to today.
        """
        today = timezone.now().date()
        one_year_ago = today - timedelta(days=365)
        return self.filter(date__gte=one_year_ago)

    def the_year_before(self):
        """
        Sales in the 12 months prior the last 12 months. The year before this last one.
        """
        today = timezone.now().date()
        one_year_ago = today - timedelta(days=365)
        two_years_ago = one_year_ago - timedelta(days=365)
        return self.filter(date__lt=one_year_ago).filter(date__gte=two_years_ago)

    def median_price(self):
        """
        The median sales price.
        """
        count = self.count()
        values = self.values_list("price", flat=True).order_by("price")
        if count % 2 == 1:
            return values[int(round(count/2))]
        else:
            return sum(values[count/2-1:count/2+1])/Decimal(2.0)

    def median_price_per_sqft(self):
        """
        The median sales price divided into the size of the unit.
        """
        count = self.count()
        inputs = self.values_list("price", "square_feet", named=True)
        values = sorted([t.price / t.square_feet for t in inputs])
        if count % 2 == 1:
            return values[int(round(count/2))]
        else:
            return sum(values[count/2-1:count/2+1])/Decimal(2.0)


class SaleManager(models.Manager):

    def get_queryset(self):
        return SaleQuerySet(self.model, using=self._db)

    def the_last_year(self):
        return self.get_queryset().the_last_year()

    def the_year_before(self):
        return self.get_queryset().the_year_before()

    def median_price(self):
        return self.get_queryset().median_price()

    def median_price_per_sqft(self):
        return self.get_queryset().median_price_per_sqft()
