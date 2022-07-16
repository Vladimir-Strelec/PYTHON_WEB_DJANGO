from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=24,
    )

    def __str__(self):
        return f'{self.name}'


class Todo(models.Model):
    title = models.CharField(
        max_length=24,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )