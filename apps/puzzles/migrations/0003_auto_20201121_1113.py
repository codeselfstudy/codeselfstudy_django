# Generated by Django 3.1.3 on 2020-11-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0002_auto_20201121_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='original_raw_data',
            field=models.JSONField(blank=True, default={}, help_text='Any Python data type here will be turned into JSONB.'),
        ),
    ]
