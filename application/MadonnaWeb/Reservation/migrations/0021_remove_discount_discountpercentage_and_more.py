# Generated by Django 4.1.3 on 2023-02-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0020_reservations_timein_reservations_timeout'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='reservations',
            name='time',
            field=models.TimeField(auto_created=True, null=True),
        ),
    ]
