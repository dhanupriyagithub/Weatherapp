# Generated by Django 4.1.4 on 2022-12-16 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("WeatherApp", "0002_alter_city_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={"verbose_name_plural": "cities"},
        ),
        migrations.AlterModelTable(
            name="city",
            table=None,
        ),
    ]
