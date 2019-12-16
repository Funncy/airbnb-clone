from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "love you~~~~~"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        )

    def handle(self, *args, **options):
        for i in range(int(options["times"])):
            print("i love you")

