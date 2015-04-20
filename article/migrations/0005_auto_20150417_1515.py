# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20150401_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 15, 15, 26, 953193, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name='Текст коментария'),
            preserve_default=True,
        ),
    ]
