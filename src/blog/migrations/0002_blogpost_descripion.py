# Generated by Django 3.1.6 on 2023-02-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="descripion",
            field=models.TextField(default=""),
        ),
    ]
