# Generated by Django 2.0.2 on 2018-02-24 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_category_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='favourite',
            new_name='like',
        ),
    ]
