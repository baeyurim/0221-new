# Generated by Django 2.2.1 on 2019-05-28 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20190526_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 28, 18, 3, 4, 823625), verbose_name='date published'),
        ),
    ]
