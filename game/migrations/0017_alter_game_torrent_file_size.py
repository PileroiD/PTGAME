# Generated by Django 3.2.2 on 2021-05-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_game_torrent_file_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='torrent_file_size',
            field=models.CharField(blank=True, default='КБ', max_length=100, null=True, verbose_name='Размер торрент-файла'),
        ),
    ]
