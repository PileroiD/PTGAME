# Generated by Django 3.2.2 on 2021-05-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0037_minsysreq_directx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrentfile',
            name='repack_author',
            field=models.CharField(choices=[('Igruha', 'Igruha'), ('Xatab', 'Xatab'), ('R.G.Механики', 'R.G.Механики'), ('SxS-Fenixx', 'SxS-Fenixx'), ('R.G.Freedom', 'R.G.Freedom'), ('SEYTER', 'SEYTER'), ('SeregA-Lus', 'SeregA-Lus'), ('qoob', 'qoob'), ('GOG', 'GOG')], max_length=100, verbose_name='Репак от'),
        ),
    ]
