# Generated by Django 3.1.4 on 2021-01-24 18:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_auto_20210124_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]