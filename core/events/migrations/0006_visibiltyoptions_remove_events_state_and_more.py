# Generated by Django 4.2.4 on 2023-09-12 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20230912_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisibiltyOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='events',
            name='state',
        ),
        migrations.AddField(
            model_name='events',
            name='visibility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.visibiltyoptions'),
        ),
    ]
