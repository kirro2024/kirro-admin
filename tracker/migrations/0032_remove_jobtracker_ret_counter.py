# Generated by Django 5.1.2 on 2024-11-20 14:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0031_rename_counter_jobtracker_ret_counter"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="jobtracker",
            name="ret_counter",
        ),
    ]
