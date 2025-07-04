# Generated by Django 2.2.13 on 2020-06-30 19:38

import datetime

from django.db import migrations, models

import NEMO.fields


class Migration(migrations.Migration):
    dependencies = [
        ("NEMO", "0020_version_3_0_0"),
    ]

    operations = [
        migrations.AddField(
            model_name="area",
            name="abuse_email",
            field=NEMO.fields.MultiEmailField(
                blank=True,
                help_text="An email will be sent to this address when users overstay in the area or in children areas (logged in with expired reservation). A comma-separated list can be used.",
                max_length=2000,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="reservation_email",
            field=NEMO.fields.MultiEmailField(
                blank=True,
                help_text="An email will be sent to this address when users create or cancel reservations in the area or in children areas. A comma-separated list can be used.",
                max_length=2000,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="physicalaccesslevel",
            name="schedule",
            field=models.IntegerField(choices=[(0, "Always"), (1, "Weekdays"), (2, "Weekends")]),
        ),
        migrations.AddField(
            model_name="physicalaccesslevel",
            name="weekdays_end_time",
            field=models.TimeField(
                blank=True, default=datetime.time(0, 0), help_text="The weekday access end time", null=True
            ),
        ),
        migrations.AddField(
            model_name="physicalaccesslevel",
            name="weekdays_start_time",
            field=models.TimeField(
                blank=True, default=datetime.time(7, 0), help_text="The weekday access start time", null=True
            ),
        ),
    ]
