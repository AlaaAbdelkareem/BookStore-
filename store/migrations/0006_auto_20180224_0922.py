# Generated by Django 2.0.2 on 2018-02-24 09:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20180224_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='read',
            field=models.ManyToManyField(blank=True, null=True, related_name='read', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='wish',
            field=models.ManyToManyField(blank=True, null=True, related_name='wish', to=settings.AUTH_USER_MODEL),
        ),
    ]
