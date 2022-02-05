# Generated by Django 4.0.2 on 2022-02-04 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_Author', models.CharField(max_length=100)),
                ('book_publisher', models.CharField(max_length=100)),
                ('book_relDate', models.DateTimeField(default=datetime.datetime(2022, 2, 4, 17, 21, 17, 5528))),
            ],
        ),
    ]