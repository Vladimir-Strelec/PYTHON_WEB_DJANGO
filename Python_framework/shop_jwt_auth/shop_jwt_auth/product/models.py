from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Product(models.Model):
    RATE_CHOICES = (
        (1, 'Alcohol'),
        (2, 'Food'),
    )
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField(default=0)
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.PositiveSmallIntegerField(choices=RATE_CHOICES, unique=True)

    def __str__(self):
        return f'{self.name, self.price, self.data_create, self.data_update}'
