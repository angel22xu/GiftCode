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

        if(GiftsCode.exists(email)):
            print 'email has exist.'
            return False

        try:
            gift.save()
            return True
        except Exception, e:
            print 'Exception', e.message
            return False


