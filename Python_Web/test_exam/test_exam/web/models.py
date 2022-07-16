from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def get_valid_character(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


class Profile(models.Model):
    MAX_LENGTH_CHARACTER = 20
    MIN_LENGTH_CHARACTER = 2
    MIN_VALUE_INTEGER = 1

    first_name = models.CharField(
        max_length=MAX_LENGTH_CHARACTER,
        validators=(MinLengthValidator(MIN_LENGTH_CHARACTER), get_valid_character),)

    last_name = models.CharField(
        max_length=MAX_LENGTH_CHARACTER,
        validators=(MinLengthValidator(MIN_LENGTH_CHARACTER), get_valid_character),)

    age = models.IntegerField(
        validators=(MinValueValidator(MIN_VALUE_INTEGER),)
    )
    image_url = models.URLField(
        blank=True,
    )

    @property
    def ful_name(self):
        return f"{self.first_name} {self.last_name}"


class Note(models.Model):
    TITLE_MAX_LENGTH = 30
    TITLE_MIN_LENGTH = 2

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=(MinLengthValidator(TITLE_MIN_LENGTH), get_valid_character)
    )
    image_url = models.URLField()
    content = models.TextField(
        null=True,
        blank=True,
    )
