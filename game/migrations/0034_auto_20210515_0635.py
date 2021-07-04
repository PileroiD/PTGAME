# Generated by Django 3.2.2 on 2021-05-15 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0033_auto_20210514_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='interface_lang',
            field=models.CharField(blank=True, choices=[('RU', 'Русский'), ('ENG', 'Английский')], max_length=255, null=True, verbose_name='Язык интерфейса'),
        ),
        migrations.AddField(
            model_name='game',
            name='voice_acting_lang',
            field=models.CharField(blank=True, choices=[('RU', 'Русский'), ('ENG', 'Английский')], max_length=255, null=True, verbose_name='Язык озвучки'),
        ),
    ]