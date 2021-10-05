from django.core.management import BaseCommand

from jobseeker import utils


class Command(BaseCommand):
    """
    Load cities and states in the correct models, only available for Brazil at the moment
    """

    def handle(self, *args, **options):
        country = "india"
        utils.load_occupations_from_file(utils.get_occupationsfilename(country))

