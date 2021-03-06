# Generated by Django 3.1.3 on 2020-11-30 02:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shorten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=255, unique=True, validators=[django.core.validators.URLValidator()])),
                ('shorten_id', models.CharField(max_length=255, unique=True, validators=[django.core.validators.URLValidator()])),
                ('ip', models.CharField(max_length=20)),
            ],
        ),
    ]
