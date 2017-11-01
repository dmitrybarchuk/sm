# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def chapter(request, chapter_slug):
    return render(request, 'chapter.html', context={

    })
