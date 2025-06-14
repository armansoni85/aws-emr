# Generated by Django 5.1.3 on 2024-12-11 12:15

import base.base_upload_handlers
import base.utils
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
            name="Certification",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="Certification Name"),
                ),
                (
                    "issued_by",
                    models.CharField(max_length=100, verbose_name="Issued By"),
                ),
                (
                    "valid_until",
                    models.DateField(blank=True, null=True, verbose_name="Valid Until"),
                ),
                (
                    "document",
                    models.FileField(
                        upload_to=base.base_upload_handlers.handle_certification_document,
                        validators=[
                            base.utils.validate_document_extension,
                            base.base_upload_handlers.handle_file_upload_limit,
                        ],
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="certifications",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Employee",
                    ),
                ),
            ],
            options={
                "verbose_name": "Certification",
                "verbose_name_plural": "Certifications",
            },
        ),
        migrations.CreateModel(
            name="DutyDetail",
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
                    "department_name",
                    models.CharField(max_length=100, verbose_name="Department"),
                ),
                ("duty_start_time", models.TimeField(verbose_name="Duty Start Time")),
                ("duty_end_time", models.TimeField(verbose_name="Duty End Time")),
                (
                    "is_on_call",
                    models.BooleanField(verbose_name="On call availability"),
                ),
                (
                    "room_number",
                    models.CharField(max_length=50, verbose_name="Consultation Room"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="duty_details",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "DutyDetails",
                "verbose_name_plural": "DutyDetail",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="ProfessionalInformation",
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
                    "speciality",
                    models.CharField(max_length=200, verbose_name="Speciality"),
                ),
                (
                    "sub_speciality",
                    models.CharField(max_length=200, verbose_name="Sub Speciality"),
                ),
                (
                    "medical_license_number",
                    models.CharField(
                        max_length=100, verbose_name="Medical License Number"
                    ),
                ),
                (
                    "years_of_experience",
                    models.FloatField(
                        blank=True, null=True, verbose_name="Experienced Year"
                    ),
                ),
                (
                    "profession_id",
                    models.CharField(unique=True, verbose_name="Profession Id"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="professional_informations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "ProfessionalInformations",
                "verbose_name_plural": "ProfessionalInformation",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Qualification",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="Qualification Name"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "organization",
                    models.CharField(
                        max_length=100, verbose_name="Granting Organization"
                    ),
                ),
                (
                    "document",
                    models.FileField(
                        upload_to=base.base_upload_handlers.handle_qualification_document,
                        validators=[
                            base.utils.validate_document_extension,
                            base.base_upload_handlers.handle_file_upload_limit,
                        ],
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qualifications",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Employee",
                    ),
                ),
            ],
            options={
                "verbose_name": "Qualification",
                "verbose_name_plural": "Qualifications",
            },
        ),
    ]
