# Generated by Django 2.2.1 on 2019-05-26 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20190519_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 21, 3, 51, 233591), verbose_name='date published'),
        ),
    ]
