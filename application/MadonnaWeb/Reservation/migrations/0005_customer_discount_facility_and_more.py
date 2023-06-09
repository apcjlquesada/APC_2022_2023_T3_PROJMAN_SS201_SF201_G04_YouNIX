# Generated by Django 4.1.3 on 2023-02-09 02:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('contactNumber', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discountCode', models.CharField(max_length=15)),
                ('discountPercentage', models.DecimalField(decimal_places=3, max_digits=3)),
                ('discountExpiration', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilityName', models.CharField(max_length=255)),
                ('facilityPrice', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='lastname',
        ),
        migrations.AddField(
            model_name='reservations',
            name='checkIn',
            field=models.DateField(default=datetime.datetime(2023, 2, 9, 2, 34, 25, 650727, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservations',
            name='checkOut',
            field=models.DateField(default=datetime.datetime(2023, 2, 9, 2, 34, 33, 827302, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservations',
            name='discounted',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservations',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 2, 9, 2, 34, 51, 129253, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
