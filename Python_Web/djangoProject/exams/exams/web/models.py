from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible


def valid_only_character(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


@deconstructible
class MaxSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError('Max file size is 5.00 MB')


class Profile(models.Model):

    MIN_VALID_CHARACTER = 2
    MAX_VALID_CHARACTER = 15

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=MAX_VALID_CHARACTER,
        validators=(MinLengthValidator(MIN_VALID_CHARACTER), valid_only_character,),)

    last_name = models.CharField(
        max_length=MAX_VALID_CHARACTER,
        validators=(MinLengthValidator(MIN_VALID_CHARACTER), valid_only_character,),)

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(MinValueValidator(BUDGET_MIN_VALUE),),
    )

    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(MaxSizeInMbValidator(IMAGE_MAX_SIZE_MB),),)

    @property
    def ful_name(self):
        return f"{self.first_name} {self.last_name}"


class Expense(models.Model):
    TITLE_MAX_LEN_CHARACTER = 30

    title = models.CharField(max_length=TITLE_MAX_LEN_CHARACTER,)

    image = models.URLField()

    price = models.FloatField()

    description = models.TextField(
        null=True,
        blank=True,
    )

