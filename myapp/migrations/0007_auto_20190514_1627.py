# Generated by Django 2.2.1 on 2019-05-14 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190514_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 16, 27, 40, 962269), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='writer',
            field=models.CharField(default='default', max_length=50),
        ),
    ]
