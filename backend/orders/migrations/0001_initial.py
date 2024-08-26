# Generated by Django 5.1 on 2024-08-26 22:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("order_id", models.CharField(max_length=255, unique=True)),
                ("transation_code", models.CharField(max_length=255, unique=True)),
                ("date", models.DateField(default="1403-06-06")),
                ("time", models.TimeField(default="02:06:27")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="accounts.customuser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.PositiveIntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="orders.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(
                through="orders.OrderItem", to="products.product"
            ),
        ),
    ]
