# Generated by Django 3.2.2 on 2021-05-15 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0042_alter_torrentfile_repack_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minsysreq',
            name='directx',
            field=models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='DirectX'),
        ),
    ]
