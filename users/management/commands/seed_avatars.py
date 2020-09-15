import random
from django.core.management.base import BaseCommand
from users.models import User
from random import shuffle, seed
from faker.providers.person.en import Provider


class Command(BaseCommand):

    help = "This command creates superuser"

    def handle(self, *args, **options):
        users = User.objects.all()
        first_names = list(set(Provider.first_names))
        seed(4321)
        shuffle(first_names)
        for user in users:
            user.avatar.delete(save=True)
            user.first_name = first_names[random.randint(1, 4300)]
        self.stdout.write(self.style.SUCCESS(f"Done!"))
