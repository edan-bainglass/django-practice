import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
# Import settings
django.setup()

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

# FAKE POP SCRIPT

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    return t


def populate(N=5):
    """Create N Entries of Dates Accessed."""

    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create new Webpage Entry
        page = Webpage.objects.get_or_create(topic=top,
                                             url=fake_url,
                                             name=fake_name)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        AccessRecord.objects.get_or_create(name=page, date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...", end=' ')
    populate(20)
    print('Done!')
