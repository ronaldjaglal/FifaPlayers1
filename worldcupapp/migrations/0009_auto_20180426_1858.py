# Generated by Django 2.0.4 on 2018-04-26 18:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('worldcupapp', '0008_auto_20180426_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]