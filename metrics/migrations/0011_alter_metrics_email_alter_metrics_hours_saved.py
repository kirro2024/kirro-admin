# Generated by Django 5.1.2 on 2024-11-20 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metrics", "0010_alter_metrics_email"),
        ("preferences", "0007_alter_userprofile_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="metrics",
            name="email",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="preferences.userprofile",
                to_field="email",
            ),
        ),
        migrations.AlterField(
            model_name="metrics",
            name="hours_saved",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
