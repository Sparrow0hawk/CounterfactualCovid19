# Generated by Django 3.1.5 on 2021-01-26 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CasesRecord",
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
                ("date", models.DateField()),
                ("cases", models.FloatField()),
                (
                    "iso_code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="countries.country",
                    ),
                ),
            ],
            options={
                "unique_together": {("iso_code", "date")},
            },
        ),
    ]
