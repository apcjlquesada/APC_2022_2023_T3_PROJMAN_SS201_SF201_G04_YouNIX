# Generated by Django 4.1.3 on 2023-01-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=50)),
            ],
        ),
    ]
