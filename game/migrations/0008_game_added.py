# Generated by Django 3.2.2 on 2021-05-07 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_game_downloads_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]