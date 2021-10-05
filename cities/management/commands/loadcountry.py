from django.core.management import BaseCommand

from cities import utils


class Command(BaseCommand):
    """
    Load cities and states in the correct models, only available for Brazil at the moment
    """

    def handle(self, *args, **options):
        country = "India"
        utils.load_country_from_file(utils.get_country_filename(country))
