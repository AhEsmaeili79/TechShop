# Generated by Django 5.1 on 2024-09-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_alter_order_date_alter_order_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="time",
            field=models.TimeField(default="22:26:47"),
        ),
    ]
