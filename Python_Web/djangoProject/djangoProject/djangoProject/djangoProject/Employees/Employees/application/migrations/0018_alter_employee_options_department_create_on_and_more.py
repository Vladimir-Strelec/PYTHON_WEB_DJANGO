# Generated by Django 4.0.1 on 2022-02-01 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0017_alter_department_name_alter_employee_egn_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('companies', 'first_name')},
        ),
        migrations.AddField(
            model_name='department',
            name='create_on',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='update_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]