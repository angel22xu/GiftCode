#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import select

from apps.db.database import Session, Base

class GiftsCode(Base):
    __tablename__ = 'gifts_code'

    email = Column(String, primary_key=True)
    code = Column(String)
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    status = Column(Integer)
    dummy1 = Column(String)
    dummy2 = Column(String)
    
    session = None

    def __init__(self, email, code):
        self.email = email
        self.code = code
        self.session = Session()

    def __repr__(self):
        '''
        Show nicely formatted GiftsCode objects.
        '''
        return "<GiftCode(email='%s', code='%s')>" % (self.email, self.code)