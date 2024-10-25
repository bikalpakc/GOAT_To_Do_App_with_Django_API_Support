# Generated by Django 5.1.1 on 2024-09-23 16:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('task_name', models.CharField(max_length=50)),
                ('task_completed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
