# Generated by Django 4.2.11 on 2024-04-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contacts",
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
                ("phone_num", models.IntegerField()),
                ("address", models.TextField(max_length=200)),
                ("address_link", models.URLField()),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
