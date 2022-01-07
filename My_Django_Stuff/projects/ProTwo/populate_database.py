import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django

# Import settings
django.setup()

from AppTwo.models import User
from faker import Faker

# FAKE POP SCRIPT


def populate(faker: Faker, N=5):

    for entry in range(N):

        fake_first_name = faker.first_name()
        fake_last_name = faker.last_name()
        fake_email = faker.email()

        User.objects.get_or_create(first_name=fake_first_name,
                                   last_name=fake_last_name,
                                   email=fake_email)


if __name__ == '__main__':
    print("Populating the databases...", end=' ')
    populate(Faker(), 20)
    print('Done!')
