# Generated by Django 4.0.1 on 2022-02-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0019_alter_department_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]