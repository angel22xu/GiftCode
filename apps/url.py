#!/usr/bin/env python
#-*- coding: utf-8 -*-

from apps.views.index import IndexHandler
from apps.views.gifts_code import GiftsCodeHandler


url =[
    (r"/", IndexHandler),
    (r"/index", IndexHandler),
    (r"/giftscode", GiftsCodeHandler),
]