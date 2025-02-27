# Generated by Django 4.2.19 on 2025-02-24 14:22

from django.db import migrations

from NEMO.migrations_utils import create_news_for_version


class Migration(migrations.Migration):

    dependencies = [
        ("NEMO", "0101_alter_emaillog_category"),
    ]

    def new_version_news(apps, schema_editor):
        create_news_for_version(apps, "7.0.1", "")

    operations = [
        migrations.RunPython(new_version_news),
    ]
