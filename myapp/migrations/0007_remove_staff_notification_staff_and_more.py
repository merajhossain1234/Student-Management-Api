# Generated by Django 5.0.1 on 2024-02-07 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_staff_notification_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff_notification',
            name='staff',
        ),
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]