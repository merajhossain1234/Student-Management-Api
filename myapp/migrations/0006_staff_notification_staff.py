# Generated by Django 5.0.1 on 2024-02-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_staff_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]
