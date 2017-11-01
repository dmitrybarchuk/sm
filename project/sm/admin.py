# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from sm.models import Chapter


class ChapterAdmin(admin.ModelAdmin):
    exclude = ()
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'created', 'modified', 'pay']
    list_filter = ['title', 'pay']


admin.site.register(Chapter, ChapterAdmin)
