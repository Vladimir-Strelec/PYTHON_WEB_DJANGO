# Generated by Django 4.0.1 on 2022-01-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_employee_firms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='companies',
            field=models.CharField(choices=[('Google', 'Google'), ('Facebook', 'Facebook'), ('Softuni', 'Softuni')], max_length=8),
        ),
    ]
