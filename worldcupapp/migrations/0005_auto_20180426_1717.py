# Generated by Django 2.0.4 on 2018-04-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldcupapp', '0004_auto_20180426_0451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='PlayerNumber',
            new_name='Number',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='NationalTeam',
            new_name='Team',
        ),
        migrations.AddField(
            model_name='player',
            name='ClubCountry',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
