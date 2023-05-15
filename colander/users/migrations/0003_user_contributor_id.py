# Generated by Django 3.2.18 on 2023-05-15 12:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contributor_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Contributor ID.'),
        ),
    ]
