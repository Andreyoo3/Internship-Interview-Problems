# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150227_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
    ]
