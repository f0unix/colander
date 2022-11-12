# Generated by Django 3.2.15 on 2022-11-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_commonmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonmodel',
            name='source_url',
            field=models.URLField(blank=True, help_text='Specify the source of this object.', null=True, verbose_name='Source URL'),
        ),
        migrations.AlterField(
            model_name='observablerelation',
            name='name',
            field=models.CharField(help_text='Name of this relation between two observables.', max_length=512),
        ),
    ]
