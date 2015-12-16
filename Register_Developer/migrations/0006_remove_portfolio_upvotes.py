# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Developer', '0005_auto_20151216_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='upvotes',
        ),
    ]
