# Generated by Django 5.1.2 on 2024-11-28 22:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0016_remove_jobtracker_applicant_uuid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobtracker",
            name="applicant_uuid",
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
