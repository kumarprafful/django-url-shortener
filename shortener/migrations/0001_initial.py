# Generated by Django 3.0.2 on 2020-01-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLs',
            fields=[
                ('short_id', models.SlugField(max_length=6, primary_key=True, serialize=False)),
                ('long_url', models.URLField(max_length=255)),
                ('short_url', models.URLField(max_length=255)),
                ('created', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
