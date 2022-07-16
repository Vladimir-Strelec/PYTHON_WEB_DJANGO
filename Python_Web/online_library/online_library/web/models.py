from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def isalpha_validation(value):
    if not value.isalpha():
        raise ValidationError('Vvedite tolko bukvi!')


class Profile(models.Model):
    MAX_LENGTH_NAMES = 30
    MIN_LENGTH_NAMES = 2

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        validators=(MinLengthValidator(MIN_LENGTH_NAMES), isalpha_validation),
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        validators=(MinLengthValidator(MIN_LENGTH_NAMES), isalpha_validation),
    )
    image_url = models.URLField()

    @property
    def action_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    MAX_LENGTH_NAMES = 30
    MIN_LENGTH_NAMES = 2
    title = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        validators=(MinLengthValidator(MIN_LENGTH_NAMES), isalpha_validation),
        verbose_name='Title',
    )
    description = models.TextField(
        null=True,
        blank=True,

    )
    image = models.URLField
    type = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        validators=(MinLengthValidator(MIN_LENGTH_NAMES), isalpha_validation),
    )
