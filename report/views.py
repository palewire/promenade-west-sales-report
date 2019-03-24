from django.conf import settings
from django.utils import timezone
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models.functions import TruncYear

# Models
from sales.models import Sale
from listings.models import Listing


class IndexView(TemplateView):
    template_name = "report/index.html"

    def get_context_data(self):
        everything = Sale.objects.select_related("building").all()
        everything_pwest = everything.filter(building__name='Promenade West')

        the_last_year = Sale.objects.select_related("building").the_last_year()
        the_last_year_pwest = the_last_year.filter(building__name='Promenade West')

        the_year_before = Sale.objects.select_related("building").the_year_before()
        the_year_before_pwest = the_year_before.filter(building__name='Promenade West')

        everything_pwest_by_year = everything_pwest.annotate(
            year=TruncYear("date")
        ).filter(
            date__year__lt=timezone.now().year
        ).values('year').annotate(count=Count("*")).order_by("year")

        listings_pwest = Listing.objects.all().order_by("-price")

        return {
            'the_last_year': the_last_year,
            'the_last_year_pwest': the_last_year_pwest,
            'the_year_before': the_year_before,
            'the_year_before_pwest': the_year_before_pwest,
            "everything": everything,
            "everything_pwest": everything_pwest,
            "everything_pwest_by_year": everything_pwest_by_year,
            "listings_pwest": listings_pwest,
        }
