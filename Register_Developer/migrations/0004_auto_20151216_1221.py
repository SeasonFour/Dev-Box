# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Developer', '0003_auto_20151216_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
