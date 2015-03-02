#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column


from apps.db.database import Base
from apps.db.database import session

class User(Base):
    __tablename__ = "user"

    uid = Column(String, primary_key=True)
    user_name = Column(String)