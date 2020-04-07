from django.core.management.base import BaseCommand, CommandError
from park.models import Park

import csv
import os.path

class Command(BaseCommand):
    help = 'Import CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        filename = options['filename']
        if not os.path.isfile(filename):
            raise CommandError('File "%s" does not exist' % filename)
        count = 0
        with open(filename, newline='') as importfile:
            importreader = csv.reader(importfile)
            hdr = next(importreader)
            for line in importreader:
                import_values = dict(zip(hdr, line))
                Park.create_entry(import_values)
                count += 1
        self.stdout.write(self.style.SUCCESS('Successfully imported %s lines' % count))
