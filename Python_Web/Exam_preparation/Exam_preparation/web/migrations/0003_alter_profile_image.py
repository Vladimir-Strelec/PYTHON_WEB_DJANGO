# Generated by Django 4.0.2 on 2022-02-26 18:27

import Exam_preparation.web.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/', validators=[Exam_preparation.web.models.MaxSizeInMbValidator(5.0)]),
        ),
    ]