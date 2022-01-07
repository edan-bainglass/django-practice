import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
# Import settings
django.setup()

import random
from AppTwo.models import User
from faker import Faker

# FAKE POP SCRIPT

fakegen = Faker()


def populate(N=5):
    """Create N Entries of Dates Accessed."""

    for entry in range(N):

        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        User.objects.get_or_create(first_name=fake_first_name,
                                   last_name=fake_last_name,
                                   email=fake_email)[0]


if __name__ == '__main__':
    print("Populating the databases...", end=' ')
    populate(20)
    print('Done!')
