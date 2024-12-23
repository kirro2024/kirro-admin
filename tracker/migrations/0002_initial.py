# Generated by Django 5.1.2 on 2024-12-19 22:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tracker", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="jobtracker",
            name="updated_by",
            field=models.ForeignKey(
                help_text="[required]",
                limit_choices_to={"is_staff": True},
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dep_update",
                to=settings.AUTH_USER_MODEL,
                to_field="email",
            ),
        ),
    ]
