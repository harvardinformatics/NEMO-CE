# Generated by Django 4.2.15 on 2024-12-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NEMO", "0094_interlockcard_extra_args"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservationquestions",
            name="enabled",
            field=models.BooleanField(default=True),
        ),
    ]
