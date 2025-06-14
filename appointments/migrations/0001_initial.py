# Generated by Django 5.1.3 on 2024-12-27 18:35

import appointments.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "appointment_datetime",
                    models.DateTimeField(verbose_name="Appointment Date"),
                ),
                ("reason_of_visit", models.TextField(verbose_name="Reason of visit")),
                (
                    "disease",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Disease"
                    ),
                ),
                (
                    "appointment_status",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending"),
                            ("IN_PROGRESS", "In Progress"),
                            ("REJECTED", "Rejected"),
                            ("DONE", "Done"),
                        ],
                        default="PENDING",
                        verbose_name="Appointment Status",
                    ),
                ),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor_appointments",
                        to=settings.AUTH_USER_MODEL,
                        validators=[appointments.validators.validate_doctor],
                        verbose_name="Doctor",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient_appointments",
                        to=settings.AUTH_USER_MODEL,
                        validators=[appointments.validators.validate_patient],
                        verbose_name="Patient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Appointment",
                "verbose_name_plural": "Appointments",
                "ordering": ["-created_at"],
            },
        ),
    ]
