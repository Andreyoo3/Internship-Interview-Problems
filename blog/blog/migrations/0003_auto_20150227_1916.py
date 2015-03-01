# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150227_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(related_name='blogs', blank=True, to='blog.Tag'),
            preserve_default=True,
        ),
    ]
