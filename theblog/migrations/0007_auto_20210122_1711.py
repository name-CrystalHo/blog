# Generated by Django 3.1.4 on 2021-01-22 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_postarticleimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostArticleImages',
            new_name='PostArticleImage',
        ),
    ]
