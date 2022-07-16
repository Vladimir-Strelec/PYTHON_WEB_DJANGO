from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible


def get_value_only_character(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


@deconstructible
class MaxSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        megabyte_limit = 15.00
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError('Max file size is 5.00 MB')


class Profile(models.Model):
    UPLOAD = 'profiles/'
    NAME_MAX_LENGTH = 15
    NAME_MIN_LENGTH = 2

    BUDGET_MIN_VALUE = 0

    MAX_SIZE_IMAGE = 5

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(MinLengthValidator(NAME_MIN_LENGTH), get_value_only_character,),
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(MinLengthValidator(NAME_MIN_LENGTH), get_value_only_character,),
    )

    budget = models.FloatField(
        default=0,
        validators=(MinValueValidator(BUDGET_MIN_VALUE),),
    )

    image = models.ImageField(
        upload_to=UPLOAD,
        null=True,
        blank=True,
        validators=(MaxSizeInMbValidator(MAX_SIZE_IMAGE),),
    )

    @property
    def profile_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    EXPENSE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=EXPENSE_MAX_LENGTH,
        validators=(get_value_only_character,),
    )

    image = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField()
