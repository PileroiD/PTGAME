# Generated by Django 3.2.2 on 2021-05-07 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_pagehit'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagehit',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game.game'),
            preserve_default=False,
        ),
    ]