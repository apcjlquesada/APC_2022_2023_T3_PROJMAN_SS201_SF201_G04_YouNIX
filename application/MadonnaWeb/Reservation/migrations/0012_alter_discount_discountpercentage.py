# Generated by Django 4.1.3 on 2023-02-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0011_facility_facilitycategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='discountPercentage',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
