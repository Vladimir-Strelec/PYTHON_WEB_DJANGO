from django.core.validators import MinLengthValidator
from django.db import models


def get_valid_character(value):
    if not value.isalpha():
        raise ValueError(f'In {value} not is valid')


class Recipe(models.Model):
    MAX_LENGTH_TITLE = 30
    MAX_LENGTH_INGREDIENTS = 30
    MIN_LENGTH_CHARACTER = 2

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        validators=(MinLengthValidator(MIN_LENGTH_CHARACTER), get_valid_character),
    )

    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(
        max_length=MAX_LENGTH_INGREDIENTS,
        validators=(MinLengthValidator(MIN_LENGTH_CHARACTER),),
    )
    time = models.TimeField()

