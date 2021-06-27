# Generated by Django 3.2.3 on 2021-06-27 21:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_auto_20210627_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
