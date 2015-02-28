#!/usr/bin/env python
#-*- coding: utf-8 -*-

import uuid
import tornado.web

from apps.models.gifts_code import GiftsCode

class GiftsCodeLogic(object):

    @staticmethod
    def add(email, code):
        '''
        create a unique code
        '''

        gift = GiftsCode(email, code)

        try:
            gift.session.add(gift)
            gift.session.commit()
            return True
        except Exception, e:
            return False


