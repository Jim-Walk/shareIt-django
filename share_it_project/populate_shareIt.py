import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'share_it_project.settings')

import django
django.setup()

from shareIt.models import Image

def populate():

    add_image("Field","user_images/drypleasentfarmland.jpg")

def add_image(name,image):
    i = Image.objects.get_or_create(name=name,image=image)[0]
    return i

populate()