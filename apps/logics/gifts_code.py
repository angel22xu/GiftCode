#!/usr/bin/env python
#-*- coding: utf-8 -*-

import uuid
import tornado.web
import thread

from apps.models.gifts_code import GiftsCode
from apps.logics.mail import Mail

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
        gift.save()


        # try:
        #     # send code to the target email
        #     if (Mail.send(email, code)):
        #         gift.save()
        #         print 'email success send'
        #         return True
        #     else:
        #         return False
        # except Exception, e:
        #     print 'email failure send'
        #     print 'Exception', e.message
        #     return False

        thread.start_new_thread(Mail.send, (email, code))

        return True