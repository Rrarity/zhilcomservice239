# -*- coding: utf-8 -*-

from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required


@login_required
@render_to("index.html")
def index(request):
    return {}
