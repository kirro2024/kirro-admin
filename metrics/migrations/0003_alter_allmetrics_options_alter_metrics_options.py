# Generated by Django 5.1.2 on 2025-02-18 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0002_allmetrics_alter_metrics_table_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="allmetrics",
            options={
                "managed": True,
                "ordering": ["id"],
                "verbose_name": "all_metrics",
                "verbose_name_plural": "all_metrics",
            },
        ),
        migrations.AlterModelOptions(
            name="metrics",
            options={
                "managed": True,
                "ordering": ["id"],
                "verbose_name": "Metrics",
                "verbose_name_plural": "Metrics",
            },
        ),
    ]
