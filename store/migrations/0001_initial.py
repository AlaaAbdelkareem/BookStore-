# Generated by Django 2.0.2 on 2018-02-21 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('pic', models.ImageField(upload_to='static/media/images')),
                ('DOB', models.DateTimeField()),
                ('DOD', models.DateTimeField(null=True)),
                ('follow', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('pic', models.ImageField(upload_to='static/media/images')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pic', models.ImageField(upload_to='static/media/images')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='cat_books',
            field=models.ManyToManyField(to='store.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='read',
            field=models.ManyToManyField(related_name='read', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.ManyToManyField(related_name='review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='wish',
            field=models.ManyToManyField(related_name='wish', to=settings.AUTH_USER_MODEL),
        ),
    ]
