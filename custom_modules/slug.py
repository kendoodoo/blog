from slugify import slugify
from random import randint

def gen(str_slug):
    jeez = slugify(str_slug, max_length=20)
    return jeez + '-' + str(randint(1000,9999))