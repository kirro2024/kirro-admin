# Generated by Django 5.1.2 on 2024-11-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0011_jobtracker_job_description_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobtracker",
            name="application_counter",
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]