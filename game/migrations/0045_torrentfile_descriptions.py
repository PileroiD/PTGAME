# Generated by Django 3.2.2 on 2021-05-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0044_auto_20210515_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='torrentfile',
            name='descriptions',
            field=models.TextField(null=True, verbose_name='Особености репака'),
        ),
    ]