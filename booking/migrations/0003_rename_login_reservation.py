# Generated by Django 4.2.16 on 2024-10-31 11:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0002_alter_reservation_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login',
            new_name='Reservation',
        ),
    ]
