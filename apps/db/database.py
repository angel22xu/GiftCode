#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.databases import mysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from apps import settings

#-------------------------------------------------------------------------------
DB_ECHO = True
DB_ENCODING = 'utf-8'

DB_INFO = 'mysql://%s:%s@%s:3306/%s?charset=utf8' %settings.DB_ACCOUNT_PASSWORD['master']
DB_ENGINE = create_engine(DB_INFO, echo = DB_ECHO, encoding = DB_ENCODING, pool_recycle = 120, pool_size = 1, max_overflow = -1)
#metadata = MetaData(DB_ENGINE)


# declare a mapping
Base = declarative_base()

Session = sessionmaker(bind=DB_ENGINE)