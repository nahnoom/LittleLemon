# Generated by Django 5.0.7 on 2024-07-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_booking_id_alter_booking_no_of_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.SmallIntegerField(),
        ),
    ]
