# Generated by Django 2.0.4 on 2018-04-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldcupapp', '0009_auto_20180426_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
