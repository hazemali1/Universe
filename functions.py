#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from galaxies import Galaxie
from solar_systems import Solar_System
from planets import Planet
from details import Detail

from db import Base


engine = create_engine("mysql+mysqldb://root:root@localhost/db_test")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
db = Session()

def save(saving=None):
	if saving:
		db.add(saving)
		db.commit()

def new(create=None):
	if create == "galaxy":
		name = input("what is the name of that galaxy? ")
		if name:
			galaxy = Galaxie(name)
			save(galaxy)
			details = input("enter the file path of details: ")
			with open(details, encoding='utf8') as f:
				reader = f.read()
			Details = Detail(reader, details_Galaxies_id=galaxy.id)
			save(Details)
			print("Done!")

def all():
	All = {}
	All["Galaxies"] = db.query(Galaxie).all()
	for keys, value in All.items():
		print(value)
