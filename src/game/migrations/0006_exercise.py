# Generated by Django 5.1.1 on 2024-10-04 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0005_joint"),
        ("organization", "0002_membership_approved_alter_membership_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="Exercise",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("description", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=50)),
                ("public", models.BooleanField(default=False)),
                (
                    "correct_word",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="correct_word",
                        to="game.word",
                    ),
                ),
                (
                    "joint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="joint",
                        to="game.joint",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization",
                        to="organization.organization",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
