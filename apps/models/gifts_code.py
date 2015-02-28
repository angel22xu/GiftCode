#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import select

from apps.db.database import Base
from apps.db.database import session


class GiftsCode(Base):
    __tablename__ = 'gifts_code'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    code = Column(String)
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    status = Column(Integer)  # 0: 初期値、引き取りしない 1:引き取りしました
    host = Column(String)
    dummy1 = Column(String)
    dummy2 = Column(String)
    
    def __init__(self, email, code):
        self.email = email
        self.code = code

    def __repr__(self):
        '''
        Show nicely formatted GiftsCode objects.
        '''
        return "<GiftCode(email='%s', code='%s')>" % (self.email, self.code)

    @classmethod
    def exists(cls, email):
        '''
        メールはもう登録したかどうか判断する
        '''
        query = session.query(cls.email)
        flag = False
        for em in query.filter(cls.email==email):
            flag = True

        return flag

    def save(self):
        '''
        レコードをインサートする
        '''
        self.create_time = datetime.datetime.now()
        self.status = 0
        session.add(self)
        session.commit()



