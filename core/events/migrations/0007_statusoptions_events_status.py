# Generated by Django 4.2.4 on 2023-09-12 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_visibiltyoptions_remove_events_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.statusoptions'),
        ),
    ]
