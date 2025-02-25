# Generated by Django 3.2.19 on 2023-05-12 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("NEMO", "0045_version_4_5_0"),
    ]

    operations = [
        migrations.AddField(
            model_name="areaaccessrecord",
            name="validated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="area_access_validated_set",
                to="NEMO.User",
            ),
        ),
        migrations.AddField(
            model_name="consumablewithdraw",
            name="validated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consumable_withdrawal_validated_set",
                to="NEMO.User",
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="validated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservation_validated_set",
                to="NEMO.User",
            ),
        ),
        migrations.AddField(
            model_name="staffcharge",
            name="validated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staff_charge_validated_set",
                to="NEMO.User",
            ),
        ),
        migrations.AddField(
            model_name="trainingsession",
            name="validated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="training_validated_set",
                to="NEMO.User",
            ),
        ),
        migrations.AddField(
            model_name="usageevent",
            name="validated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="usage_event_validated_set",
                to="NEMO.User",
            ),
        ),
    ]
