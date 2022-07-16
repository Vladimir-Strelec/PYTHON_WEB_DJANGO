from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=10)
    text = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.title}"
