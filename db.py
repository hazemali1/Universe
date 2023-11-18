#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("mysql+mysqldb://root:root@localhost/db_test")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
db = Session()
