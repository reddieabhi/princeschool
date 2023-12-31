# Generated by Django 4.2.4 on 2023-11-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myschool", "0003_studentdetails_st_standard"),
    ]

    operations = [
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("unit_id", models.IntegerField(auto_created=True, unique=True)),
                ("unit_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="Marks",
        ),
    ]
