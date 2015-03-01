# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]
