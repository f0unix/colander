# Generated by Django 3.2.15 on 2022-11-09 17:52

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20221109_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attributes',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True),
        ),
    ]
