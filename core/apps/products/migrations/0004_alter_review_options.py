# Generated by Django 5.1.4 on 2025-01-09 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_review"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="review",
            options={
                "verbose_name": "Отзывы продуктов",
                "verbose_name_plural": "Отзывы продуктов",
            },
        ),
    ]
