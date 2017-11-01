# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse
from sorl.thumbnail import ImageField


class Chapter(models.Model):
    title = models.CharField(max_length=150, verbose_name=u'Название главы')
    slug = models.SlugField(max_length=150,)
    image = ImageField(upload_to='chapters/', blank=True, verbose_name=u'Изображение главы')
    description = models.TextField(verbose_name=u'Текст главы')
    pay = models.BooleanField(default=False, verbose_name=u'Платная глава?', help_text=u'Отметьте, если глава платная')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    modified = models.DateTimeField(auto_now=True, verbose_name=u'Дата и время последнего изменения')

    class Meta:
        verbose_name = u'Глава'
        verbose_name_plural = u'Главы'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('chapter', args=[self.slug])
