# Generated by Django 3.2.2 on 2021-05-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_delete_pagehit'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='downloads_count',
            field=models.IntegerField(default=0),
        ),
    ]
