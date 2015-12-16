# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Developer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='upvotes',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
