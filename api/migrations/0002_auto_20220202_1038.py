# Generated by Django 3.0 on 2022-02-02 05:08

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to=api.models.nameFile),
        ),
    ]
