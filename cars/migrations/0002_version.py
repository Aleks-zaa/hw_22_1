# Generated by Django 5.0.6 on 2024-06-15 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="название версии"),
                ),
                (
                    "number",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Цена за покупку"
                    ),
                ),
                ("sign", models.BooleanField(default=False, verbose_name="неактивен")),
                (
                    "car",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="version",
                        to="cars.product",
                        verbose_name="Машина",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
