# Generated by Django 2.1 on 2018-08-19 02:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 19, 2, 48, 48, 474776, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]