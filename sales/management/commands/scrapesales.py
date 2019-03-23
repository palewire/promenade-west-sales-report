import time
import requests
from bs4 import BeautifulSoup
from sales.models import Sale
from buildings.models import Building
from django.core.management.base import BaseCommand
from dateutil.parser import parse as dateparse


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        building_list = Building.objects.all()
        print(f"Scraping sales for {len(building_list)} buildings")
        for building in building_list:
            print(f"Scraping sales for {building}")

            # Request the data
            payload = dict(building_url="the-promenade-west-lofts-condos-for-sale-lease-downtown-losangeles")
            r = requests.post(building.raw_data_url, data=payload)

            # Parse out the listings
            soup = BeautifulSoup(r.text, "html5lib")
            li_list = soup.find_all("li", {"class": "leased-prop"})

            # Loop through them
            for raw_li in li_list:
                # Clean em up
                try:
                    parsed_li = self.parse_li(raw_li)
                except Exception:
                    print("Count not parse\n {}".format(raw_li))

                # Reconcile them with the database
                try:
                    obj = Sale.objects.get(url=parsed_li['url'])
                    print(f"Sale of {obj} already logged")
                    for attr, value in parsed_li.items():
                        current_value = getattr(obj, attr)
                        if current_value != value:
                            print(f"Updating {attr} from {current_value} to {value}")
                            setattr(obj, attr, value)
                            obj.save()
                except Sale.DoesNotExist:
                    print(f"Creating sale for {parsed_li['url']}")
                    parsed_li['building'] = building
                    obj = Sale.objects.create(**parsed_li)
                    print(f"Created {obj}")

            # Sleep before you start the next building
            time.sleep(3)

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
        return dict(
            url=li.a['href'],
            unit=parts[1].strip(),
            price=self.safe_price(parts[3]),
            date=dateparse(parts[4]).date(),
            bedrooms=self.safe_beds(parts[5]),
            bathrooms=self.safe_baths(parts[5]),
            square_feet=self.safe_sqft(parts[6])
        )
