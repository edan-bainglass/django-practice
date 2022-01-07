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


def populate(faker: Faker, N=5):

    for _ in range(N):

        # get the topic for the entry
        topic = Topic.objects.get_or_create(name=random.choice(TOPICS))[0]

        # Create the fake data for that entry
        fake_url = faker.url()
        fake_date = faker.date()
        fake_name = faker.company()

        # Create new Webpage Entry
        page = Webpage.objects.get_or_create(topic=topic,
                                             url=fake_url,
                                             name=fake_name)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        AccessRecord.objects.get_or_create(name=page, date=fake_date)


TOPICS = (
    'Search',
    'Social',
    'Marketplace',
    'News',
    'Games',
)

if __name__ == '__main__':
    print("Populating the databases... ", end=' ')
    populate(Faker(), 20)
    print('done!')
