import unicodedata
import csv
import itertools
import os

from django.conf import settings

from cities import models


def get_states_filename(country):
    return os.path.join(settings.CITIES_DATA_LOCATION, country.lower(), "states.csv")


def get_cities_filename(country):
    return os.path.join(settings.CITIES_DATA_LOCATION, country.lower(), "cities.csv")


def get_country_filename(country):
    return os.path.join(settings.CITIES_DATA_LOCATION, country.lower(), "countries.csv")


def load_file(filename):
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_country_from_file(filename):
    countries = load_file(filename)

    for country in countries:
        models.CountryName.objects.get_or_create(
            Country=country.get("Country"),
            Region=country.get("Region"),
            Population=country.get("Population"),
            Area=country.get("Area"),
            Pop_Density=country.get("PopDensity"),
            Coastline=country.get("Coastline"),
            Net_migration=country.get("Netmigration"),
            Infant_mortality=country.get("Infantmortality"),
            GDP=country.get("GDP"),
            Literacy=country.get("Literacy"),
            Phones=country.get("Phones"),
            Arable=country.get("Arable"),
            Crops=country.get("Crops"),
            Other=country.get("Other"),
            Climate=country.get("Climate"),
            Birthrate=country.get("Birthrate"),
            Deathrate=country.get("Deathrate"),
            Agriculture=country.get("Agriculture"),
            Industry=country.get("Industry"),
            Service=country.get("Service"),

        )


def load_states_from_file(filename):
    states = load_file(filename)

    for state in states:
        models.State.objects.get_or_create(
            code=state.get("code"), abbr=state.get("abbr"), name=state.get("name")
        )


def load_cities_from_file(filename):
    cities = load_file(filename)
    cities = sorted(cities, key=lambda c: c["state"])
    grouped_cities = itertools.groupby(cities, key=lambda c: c["state"])

    for state_abbr, cities in grouped_cities:
        # print(state_abbr)
        states = models.State.objects.get(name=state_abbr)
        con = states
        # print (states)

        for city in cities:
            models.City.objects.get_or_create(
                state=states, code=city.get("code"), name=city.get("name"))

            # print(city.get("name"))


def clear_text(txt):
    normalized_text = unicodedata.normalize("NFD", txt)
    non_comb = "".join(
        c for c in normalized_text if not unicodedata.combining(c) and c not in ["~", "´", "`", "¨", "^"]
    )
    return unicodedata.normalize("NFC", non_comb)
