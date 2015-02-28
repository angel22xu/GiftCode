#!/usr/bin/env python
#-*- coding: utf-8 -*-

import uuid
import json
import tornado.web

from apps.logics.gifts_code import GiftsCodeLogic

class GiftsCodeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('gifts_code.html')

    def post(self):
        '''
        create a unique code
        '''
        email = self.get_argument('email')
        code=uuid.uuid1().hex

        #flagはTrueの場合は正常にinsert，Falseの場合は異常
        flag = GiftsCodeLogic.add(email, code)

        result = "OK" if flag else "NG"
        code = code if flag else ""

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"code":code, "result": result}))