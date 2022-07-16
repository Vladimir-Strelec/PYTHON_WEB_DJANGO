from django.core.exceptions import ValidationError
from django.db import models
from django.core import validators


def validate_positive(value):
    if value <= 0:
        raise ValidationError('Value most be positive')


class AuditEntity(models.Model):
    create_on = models.DateTimeField(
        auto_now_add=True
    )
    update_on = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class Department(AuditEntity):
    name = models.CharField(
        max_length=40
    )

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    SOFT_WARE_DEV = 1
    QA_ENGINEER = 2

    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    SOFTUNI_BG_INTERACTIVE = 'Softuni'

    JOBS_ALL = (SOFT_WARE_DEV, QA_ENGINEER)
    COMPANIS = (GOOGLE, FACEBOOK, SOFTUNI_BG_INTERACTIVE)

    first_name = models.CharField(
        max_length=20,

    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        default='NO NAME'
    )

    image = models.ImageField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(validate_positive,),
    )

    egn = models.IntegerField(
        null=True,
        blank=True,
        unique=True,
        validators=(
            validators.MinValueValidator(10),
        ),
        verbose_name="EGN",
    )

    job_title = models.IntegerField(
        choices=(
            (SOFT_WARE_DEV, 'Software developer'),
            (QA_ENGINEER, 'Qa'),
        )
    )

    companies = models.CharField(
        max_length=max([len(name) for name in COMPANIS]),
        choices=([(c, c) for c in COMPANIS])
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('companies', 'first_name',)


class Project(models.Model):
    name = models.CharField(
        max_length=20,
        blank=True,
    )

    employees = models.ManyToManyField(
        to=Employee,
    )


class User(models.Model):
    email = models.EmailField()
    employees = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )

