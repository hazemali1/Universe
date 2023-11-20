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
			details = input("enter the file path of galaxy details: ")
			with open(details, encoding='utf8') as f:
				reader = f.read()
			Details = Detail(reader, details_Galaxies_id=galaxy.id)
			save(Details)
			print("Done create galaxy!")
	elif create == "solar_system":
		name = input("what is the name of that solar_system? ")
		name_of_galaxy = input("Enter the name of galaxy include this solar_system: ")
		galaxy_id = get_galaxy_id(name_of_galaxy)
		if name:
			if galaxy_id:
				galaxy_id = galaxy_id
			else:
				print("this galaxy does not exist. do you want to create new one? (y/n)")
				answer = input()
				if answer == "y":
					new("galaxy")
					galaxy_id = get_galaxy_id(name_of_galaxy)
				elif answer == "n":
					return
				else:
					print("please enter (y/n)")
			solar_system = Solar_System(name, galaxie_id=galaxy_id)
			save(solar_system)
			details = input("enter the file path of solar system details: ")
			with open(details, encoding='utf8') as f:
				reader = f.read()
			Details = Detail(reader, details_Solar_Systems_id=solar_system.id)
			save(Details)
			print("Done create solar system!")
	elif create == "planet":
		name = input("what is the name of that planet? ")
		name_of_solar_system = input("Enter the name of solar system include this planet: ")
		solar_system_id = get_Solar_System_id(name_of_solar_system)
		if name:
			if solar_system_id:
				solar_system_id = solar_system_id
			else:
				print("this solar system does not exist. do you want to create new one? (y/n)")
				answer = input()
				if answer == "y":
					new("solar_system")
					solar_system_id = get_Solar_System_id(name_of_solar_system)
				elif answer == "n":
					return
				else:
					print("please enter (y/n)")
			planet = Planet(name, solar_system_id=solar_system_id)
			save(planet)
			details = input("enter the file path of planet details: ")
			with open(details, encoding='utf8') as f:
				reader = f.read()
			Details = Detail(reader, details_Planets_id=planet.id)
			save(Details)
			print("Done create planet!")
	else:
		print("syntax error!!")

def all():
	All = {}
	All["Galaxies"] = db.query(Galaxie).all()
	All["Solar_Systems"] = db.query(Solar_System).all()
	All["Planets"] = db.query(Planet).all()
	for keys, value in All.items():
		print(keys + ":")
		for v in value:
			print(" " + v.name)

def get_galaxy_id(name=None):
	All = {}
	All["Galaxies"] = db.query(Galaxie).all()
	for keys, value in All.items():
		for v in value:
			if v.name == name:
				return v.id
	return None

def get_Solar_System_id(name=None):
	All = {}
	All["Solar_Systems"] = db.query(Solar_System).all()
	for keys, value in All.items():
		for v in value:
			if v.name == name:
				return v.id
	return None

def get_Planet_id(name=None):
	All = {}
	All["Planets"] = db.query(Planet).all()
	for keys, value in All.items():
		for v in value:
			if v.name == name:
				return v.id
	return None

def count(name=None):
	All = {}
	counter = 0
	if name == "galaxies":
		All["Galaxies"] = db.query(Galaxie).all()
	elif name == "solar_systems":
		All["Solar_Systems"] = db.query(Solar_System).all()
	elif name == "planets":
		All["Planets"] = db.query(Planet).all()
	else:
		print(name)
		print("syntax error!!")
	for keys, value in All.items():
		for v in value:
			counter += 1
	if counter:
		print("number of {} => {}".format(name, counter))
