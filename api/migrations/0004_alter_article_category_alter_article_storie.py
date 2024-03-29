# Generated by Django 4.0.5 on 2022-12-02 09:50

import ckeditor.fields
from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220417_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='storie',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
