#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smtplib
import mimetypes

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from apps import settings

class Mail(object):

    @classmethod
    def send(cls, receiver, code):
        '''
        send mail
        '''
        msg = 'gift code', code

        msg = MIMEMultipart()
        msg['From'] = settings.FRROMADDR
        msg['To'] = receiver
        msg['Subject'] = 'Gift Code'

        #メール内容を追加
        txt = MIMEText("CODE: " + code)
        msg.attach(txt)

        try:
            # The actual mail send
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(settings.MAIL_USERNAEME,settings.MAIL_PASSWORD)
            # server.sendmail(settings.FRROMADDR, receiver, str(msg))
            server.sendmail(settings.FRROMADDR, receiver, msg.as_string())
            server.quit()
            return True
        except Exception, e:
            return False