#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smtplib

from apps import settings

class Mail(object):

    @classmethod
    def send(cls, receiver, code):
        '''
        send mail
        '''
        msg = 'gift code', code

        try:
            # The actual mail send
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(settings.MAIL_USERNAEME,settings.MAIL_PASSWORD)
            server.sendmail(settings.FRROMADDR, receiver, str(msg))
            server.quit()
            return True
        except Exception, e:
            return False


