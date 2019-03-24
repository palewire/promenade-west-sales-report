from sales.models import Sale
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "report/index.html"

    def get_context_data(self):
        the_last_year = Sale.objects.select_related("building").the_last_year()
        the_last_year_pwest = the_last_year.filter(building__name='Promenade West')
        the_year_before = Sale.objects.select_related("building").the_year_before()
        the_year_before_pwest = the_year_before.filter(building__name='Promenade West')
        return {
            'the_last_year': the_last_year,
            'the_last_year_pwest': the_last_year_pwest,
            'the_year_before': the_year_before,
            'the_year_before_pwest': the_year_before_pwest,
        }
