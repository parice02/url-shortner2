# Generated by Django 4.2.7 on 2023-11-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URLShort",
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
                ("long_url", models.URLField()),
                ("short_url", models.URLField()),
                ("is_active", models.BooleanField(default=True)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
