#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os.path, sys
reload(sys)
sys.setdefaultencoding('utf-8')

TOP_DIR = os.path.dirname(sys.path[0])

sys.path[0] = TOP_DIR

sys.path.insert(1, os.path.join(TOP_DIR, 'libs'))

import tornado.web
from tornado.options import define, options
from apps.url import url

settings = dict(
    debug=True,
    template_path=os.path.join(TOP_DIR, 'templates'),
    static_path=os.path.join(TOP_DIR, "static")    
)


app = tornado.web.Application(
    handlers=url, **settings

)

define("port", default=8000, help="run on the given port", type=int)
def main():
    options.parse_command_line()
    app.listen(options.port, xheaders=True)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
