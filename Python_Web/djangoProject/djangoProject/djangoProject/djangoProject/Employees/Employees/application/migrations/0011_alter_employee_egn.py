# Generated by Django 4.0.1 on 2022-01-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_alter_employee_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='egn',
            field=models.IntegerField(blank=True, max_length=11, null=True, unique=True, verbose_name='EGN'),
        ),
    ]
