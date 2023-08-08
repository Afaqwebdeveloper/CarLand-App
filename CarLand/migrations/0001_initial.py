# Generated by Django 4.2.3 on 2023-08-07 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ad",
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
                ("title", models.CharField(max_length=200)),
                ("year", models.PositiveIntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField()),
                ("date_published", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="CarBrand",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="CarModel",
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
                ("name", models.CharField(max_length=100)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="CarLand.carbrand",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CarFeature",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "cars",
                    models.ManyToManyField(related_name="features", to="CarLand.ad"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="ad",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="CarLand.carbrand"
            ),
        ),
        migrations.AddField(
            model_name="ad",
            name="model",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="CarLand.carmodel"
            ),
        ),
        migrations.AddField(
            model_name="ad",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]