import requests
from bs4 import BeautifulSoup
from listings.models import Listing
from django.core.management.base import BaseCommand
from dateutil.parser import parse as dateparse


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print(f"Scraping listings for Promenade West")

        print(f"Flushing {Listing.objects.count()} records from the database")
        Listing.objects.all().delete()

        # Request the data
        url = "https://www.dlxco.com/the-promenade-west-lofts-condos-for-sale-lease-downtown-losangeles"
        r = requests.get(url)

        # Parse out the listings
        soup = BeautifulSoup(r.text, "html5lib")
        li_list = soup.find_all("li", {"class": "for-sale-listing"})

        # Loop through them
        for raw_li in li_list:
            # Clean em up
            try:
                parsed_li = self.parse_li(raw_li)
            except Exception:
                print("Count not parse\n {}".format(raw_li))
                continue

            # Save them to the database
            obj = Listing.objects.create(**parsed_li)
            print(f"Created {obj}")

    def safe_price(self, value):
        return int(value.replace("$", "").replace(",", ""))

    def safe_beds(self, value):
        return int(value.split("/")[0].replace("BR", ""))

    def safe_baths(self, value):
        return int(value.split("/")[1].replace("BATHS", "").replace(",", ""))

    def safe_sqft(self, value):
        return int(value.replace(",", ""))

    def parse_li(self, li):
        parts = li.a.text.split()
        if parts[1].strip() == '-':
            return dict(
                url=li.a['href'],
                unit='',
                price=self.safe_price(parts[2]),
                bedrooms=self.safe_beds(parts[4]),
                bathrooms=self.safe_baths(parts[4]),
                square_feet=self.safe_sqft(parts[5])
            )
        else:
            return dict(
                url=li.a['href'],
                unit=parts[1].strip(),
                price=self.safe_price(parts[3]),
                bedrooms=self.safe_beds(parts[5]),
                bathrooms=self.safe_baths(parts[5]),
                square_feet=self.safe_sqft(parts[6])
            )
