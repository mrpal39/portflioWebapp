import csv

import itertools
import os
from .models import Occupation
from django.conf import  settings




def get_occupationsfilename(country):
    return os.path.join(settings.OCCUPATIONS_DATA_LOCATION,country.lower(),"occupations.csv")


def load_file(filename):
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_occupations_from_file(filename):
    occupations=load_file(filename)
    # print(occupations)

    for occupation in occupations:
        Occupation.objects.get_or_create(
            name=occupation.get("occupations"),

        )



