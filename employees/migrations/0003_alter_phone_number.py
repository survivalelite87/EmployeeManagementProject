# Generated by Django 4.1.7 on 2024-10-16 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_remove_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(max_length=15),
        ),
    ]
