# Generated by Django 4.0.1 on 2022-02-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0022_employee_image_alter_department_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]