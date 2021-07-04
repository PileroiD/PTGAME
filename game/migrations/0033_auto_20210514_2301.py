# Generated by Django 3.2.2 on 2021-05-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0032_auto_20210514_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='category',
        ),
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ManyToManyField(to='game.Category', verbose_name='Категория'),
        ),
    ]