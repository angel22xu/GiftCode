#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    '''
    the main page
    '''

    def get(self):
        self.render('index.html')