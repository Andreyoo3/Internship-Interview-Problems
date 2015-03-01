# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_tag_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=60)),
                ('body', models.TextField()),
                ('post', models.ForeignKey(to='blog.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
