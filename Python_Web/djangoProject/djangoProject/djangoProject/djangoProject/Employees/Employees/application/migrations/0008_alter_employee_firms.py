# Generated by Django 4.0.1 on 2022-01-30 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_alter_employee_firms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='companies',
            field=models.CharField(choices=[(1, 1), (2, 2)], max_length=8),
        ),
    ]
