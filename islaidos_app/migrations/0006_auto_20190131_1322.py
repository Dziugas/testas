# Generated by Django 2.1.3 on 2019-01-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('islaidos_app', '0005_keeper_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensetypes',
            name='aktyvus',
            field=models.BooleanField(default=None),
        ),
    ]
