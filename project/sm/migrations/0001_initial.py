# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u043b\u0430\u0432\u044b')),
                ('slug', models.SlugField(max_length=150)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='chapters/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0433\u043b\u0430\u0432\u044b')),
                ('description', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0433\u043b\u0430\u0432\u044b')),
                ('pay', models.BooleanField(default=False, help_text='\u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435, \u0435\u0441\u043b\u0438 \u0433\u043b\u0430\u0432\u0430 \u043f\u043b\u0430\u0442\u043d\u0430\u044f', verbose_name='\u041f\u043b\u0430\u0442\u043d\u0430\u044f \u0433\u043b\u0430\u0432\u0430?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0413\u043b\u0430\u0432\u0430',
                'verbose_name_plural': '\u0413\u043b\u0430\u0432\u044b',
            },
        ),
    ]
