# Generated by Django 4.2.16 on 2024-10-31 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='time',
            field=models.CharField(choices=[('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00')], max_length=10),
        ),
    ]
