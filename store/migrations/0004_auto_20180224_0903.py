# Generated by Django 2.0.2 on 2018-02-24 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_auto_20180223_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='review',
        ),
        migrations.AddField(
            model_name='rate',
            name='bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Book'),
        ),
        migrations.AddField(
            model_name='rate',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
