from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        titles = ['Cozy Cottage', 'Modern Apartment', 'Luxury Villa', 'Beach House']
        locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Naivasha']

        for i in range(10):
            Listing.objects.create(
                title=random.choice(titles),
                description="This is a lovely place to stay.",
                price_per_night=round(random.uniform(50, 500), 2),
                location=random.choice(locations),
                available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))