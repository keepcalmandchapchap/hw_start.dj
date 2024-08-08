import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('dj-homeworks\\2.1-databases\\work_with_database\\phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            slug_new_phone = phone['name'].lower().replace(' ', '-')
            new_phone = Phone.objects.create(name=phone['name'],
                                            image=phone['image'],
                                            price=phone['price'],
                                            release_date=phone['release_date'],
                                            lte_exists=phone['lte_exists'],
                                            slug=slug_new_phone)
            
