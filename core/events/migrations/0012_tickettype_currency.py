# Generated by Django 4.2.4 on 2023-09-12 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fundamentals', '0007_currency'),
        ('events', '0011_alter_events_location_tickettype'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fundamentals.currency'),
        ),
    ]