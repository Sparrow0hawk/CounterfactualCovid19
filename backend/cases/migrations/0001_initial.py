# Generated by Django 3.1.5 on 2021-01-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TotalCases",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("iso_code", models.CharField(max_length=3)),
                ("cumulative_cases", models.PositiveIntegerField()),
                ("population", models.PositiveIntegerField()),
            ],
        ),
    ]
