# Generated by Django 5.2 on 2025-04-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='release_date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
