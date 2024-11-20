# Generated by Django 5.1.2 on 2024-11-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0012_jobtracker_application_counter"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobtracker",
            name="job_preferences",
            field=models.JSONField(
                default={
                    "jobEmployments": [],
                    "jobLevels": [],
                    "jobLocations": [],
                    "jobRoles": [],
                }
            ),
        ),
    ]