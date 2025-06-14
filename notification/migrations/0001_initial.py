# Generated by Django 5.1.3 on 2024-11-24 14:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationSent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('notification_type', models.CharField(blank=True, choices=[('LOGIN', 'logged_in'), ('CONTRACT_CREATED', 'contract_created'), ('CREDIT_CONSUMED', 'credit_consumed')], max_length=100, null=True, verbose_name='Notification Type')),
                ('device_type', models.CharField(blank=True, choices=[('ANDROID', 'android'), ('IOS', 'ios'), ('WEB', 'web')], max_length=100, null=True, verbose_name='Device Type')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('body', models.CharField(max_length=500, verbose_name='Body')),
                ('is_notification_seen', models.BooleanField(default=False, verbose_name='Is Notification Seen')),
                ('is_sent', models.BooleanField(default=False, verbose_name='Is Sent')),
                ('fmc_registration_token', models.TextField(blank=True, null=True, verbose_name='FMC Registration Token')),
            ],
            options={
                'verbose_name': 'Notifications',
                'verbose_name_plural': 'Notification',
                'ordering': ('-created_at',),
            },
        ),
    ]
