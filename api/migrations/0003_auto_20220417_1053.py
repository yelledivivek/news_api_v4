# Generated by Django 3.0 on 2022-04-17 05:23

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220202_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, max_length=350, null=True, upload_to=api.models.nameFile),
        ),
    ]
