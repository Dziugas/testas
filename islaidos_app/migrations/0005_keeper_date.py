# Generated by Django 2.1.3 on 2019-01-31 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('islaidos_app', '0004_auto_20190127_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='keeper',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
