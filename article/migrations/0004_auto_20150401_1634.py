# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20150401_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='commets_article',
            new_name='comments_article',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='commets_text',
            new_name='comments_text',
        ),
    ]
