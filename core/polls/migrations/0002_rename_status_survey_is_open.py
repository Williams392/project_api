# Generated by Django 4.2.4 on 2023-08-22 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='status',
            new_name='is_open',
        ),
    ]
