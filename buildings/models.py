from django.db import models


class Building(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=500)
    REGION_CHOICES = (
        ("Arts District", "Arts District"),
        ("Bunker Hill", "Bunker Hill"),
        ("City West", "City West"),
        ("Fashion District", "Fashion District"),
        ("Jewelry District", "Jewelry District"),
        ("Financial District", "Financial District"),
        ("Historic Core", "Historic Core"),
        ("L.A. Live", "L.A. Live"),
        ("Little Tokyo", "Little Tokyo"),
    )
    region = models.CharField(max_length=500, choices=REGION_CHOICES)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    @property
    def raw_data_url(self):
        return f'https://www.dlxco.com/property/getproperty/name/R-Listing/value/240/building/{self.id}'
