# Generated by Django 3.2.2 on 2021-05-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0021_alter_torrentfile_repack_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrentfile',
            name='repack_author',
            field=models.CharField(choices=[('Igruha', 'Igruha'), ('Xatab', 'Xatab'), ('R.G.Механики', 'R.G.Механики'), ('SxS-Fenixx', 'SxS-Fenixx'), ('R.G.Freedom', 'R.G.Freedom'), ('SEYTER', 'SEYTER')], max_length=100, verbose_name='Репак от'),
        ),
    ]
