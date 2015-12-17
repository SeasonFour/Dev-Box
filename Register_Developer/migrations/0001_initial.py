# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user_name', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('bio', models.TextField(verbose_name='About You', max_length=500)),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
                ('website_url', models.URLField(null=True)),
                ('years_exp', models.IntegerField(blank=True, default=1, verbose_name='Years of experience', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('software_title', models.CharField(blank=True, default='Back-End', max_length=50)),
                ('languages', models.CharField(blank=True, verbose_name='Programming Languages', max_length=1000)),
                ('is_developer', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='portfolios')),
                ('description', models.TextField()),
                ('github_link', models.URLField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='Register_Developer.Developer')),
            ],
        ),
    ]
