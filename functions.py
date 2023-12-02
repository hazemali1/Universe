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
		print("syntax error!!")
	for keys, value in All.items():
		for v in value:
			counter += 1
	if counter:
		print("number of {} => {}".format(name, counter))

def delete(name=None):
	object_to_delete = None
	Detail_to_delete = None
	Planets_to_delete = None
	solar_systems_to_delete = None
	element = input("enter name of {} you wanna remove: ".format(name))
	if name == "galaxy":
		element_id = get_galaxy_id(element)
		object_to_delete = db.query(Galaxie).filter_by(id=element_id).first()
		Detail_to_delete = db.query(Detail).filter_by(details_Galaxies_id=element_id).first()
		solar_systems_to_delete = db.query(Solar_System).filter_by(galaxie_id=element_id).all()
	elif name == "solar_system":
		element_id = get_Solar_System_id(element)
		object_to_delete = db.query(Solar_System).filter_by(id=element_id).first()
		Detail_to_delete = db.query(Detail).filter_by(details_Solar_Systems_id=element_id).first()
		Planets_to_delete = db.query(Planet).filter_by(solar_system_id=element_id).all()
	elif name == "planet":
		element_id = get_Planet_id(element)
		object_to_delete = db.query(Planet).filter_by(id=element_id).first()
		Detail_to_delete = db.query(Detail).filter_by(details_Planets_id=element_id).first()
	else:
		print("syntax error!!")
	if Planets_to_delete:
		for ele in Planets_to_delete:
			Details_to_delete = db.query(Detail).filter_by(details_Planets_id=ele.id).first()
			db.delete(Details_to_delete)
			db.delete(ele)
	if solar_systems_to_delete:
		for ele in solar_systems_to_delete:
			Planets_to_delete = db.query(Planet).filter_by(solar_system_id=ele.id).all()
			for obj in Planets_to_delete:
				Details_to_delete = db.query(Detail).filter_by(details_Planets_id=obj.id).first()
				db.delete(Details_to_delete)
				db.delete(obj)
			Details_to_delete = db.query(Detail).filter_by(details_Solar_Systems_id=ele.id).first()
			db.delete(Details_to_delete)
			db.delete(ele)
	if object_to_delete and Detail_to_delete:
		db.delete(object_to_delete)
		db.delete(Detail_to_delete)
		db.commit()
		print("Deleted complet!!")
	else:
		print("not found!!")

def show_detail(name=None):
	obj = input("enter name of {}: ".format(name))
	All = {}
	get_id = None
	if name == "galaxy":
		All["Galaxies"] = db.query(Detail).all()
		get_id = get_galaxy_id(obj)
	elif name == "solar_system":
		get_id = get_Solar_System_id(obj)
		All["Solar_Systems"] = db.query(Detail).all()
	elif name == "planet":
		get_id = get_Planet_id(obj)
		All["Planets"] = db.query(Detail).all()
	else:
		print("syntax error!!")
		return
	if get_id:
		for keys, value in All.items():
			for v in value:
				if name == "galaxy":
					det = v.details_Galaxies_id
				if name == "solar_system":
					det = v.details_Solar_Systems_id
				if name == "planet":
					det = v.details_Planets_id
				if det == get_id:
					print(v.details)
	else:
		print("not found!!")

def update(name=None):
	element = input("enter name of {} to update: ".format(name))
	detail_to_update = None
	if name == "galaxy":
		detail_id = get_galaxy_id(element)
		detail_to_update = db.query(Detail).filter_by(details_Galaxies_id=detail_id).first()
	elif name == "solar_system":
		detail_id = get_Solar_System_id(element)
		detail_to_update = db.query(Detail).filter_by(details_Solar_Systems_id=detail_id).first()
	elif name == "planet":
		detail_id = get_Planet_id(element)
		detail_to_update = db.query(Detail).filter_by(details_Planets_id=detail_id).first()
	else:
		print("syntax error!!")
	if detail_to_update:
		details = input("enter the file path of New galaxy details: ")
		with open(details, encoding='utf8') as f:
			reader = f.read()
		detail_to_update.details = reader
		db.commit()
		print("success!!")
	else:
		print("not found!!")

def get_classname(element):
	class_name = ""
	for i in element:
		if i == ' ':
			class_name += '_'
		else:
			class_name += i
	if class_name[0].isdigit():
		class_name = "_" + class_name
	return class_name

def api_universe():
	All = []
	All_Galaxies = db.query(Galaxie).all()
	All_Solar_Systems = db.query(Solar_System).all()
	All_Planets = db.query(Planet).all()
	for g in All_Galaxies:
		dic = {}
		dic['galaxy'] = g.name
		dic['galaxy_classname'] = get_classname(g.name)
		dic['solar_systems'] = []
		for s in All_Solar_Systems:
			dic_solar_system = {}
			if s.galaxie_id == g.id:
				dic_solar_system['solar_system'] = s.name
				dic_solar_system['solar_system_classname'] = get_classname(s.name)
				dic_solar_system['planets'] = []
				for p in All_Planets:
					dic_planet = {}
					if p.solar_system_id == s.id:
						dic_planet['planet'] = p.name
						dic_planet['planet_classname'] = get_classname(p.name)
						dic_solar_system['planets'].append(dic_planet)
				dic['solar_systems'].append(dic_solar_system)
		All.append(dic)
	return All

def get_galaxy_name(id=None):
	All = {}
	All["Galaxies"] = db.query(Galaxie).all()
	for keys, value in All.items():
		for v in value:
			if v.id == id:
				return v.name
	return None

def get_Solar_System_name(id=None):
	All = {}
	All["Solar_Systems"] = db.query(Solar_System).all()
	for keys, value in All.items():
		for v in value:
			if v.id == id:
				print("s")
				return v.name
	return None

def get_Planet_name(id=None):
	All = {}
	All["Planets"] = db.query(Planet).all()
	for keys, value in All.items():
		for v in value:
			if v.id == id:
				return v.name
	return None

def api_details():
	All = []
	All_Details = db.query(Detail).all()
	for details in All_Details:
		dic = {}
		dic['details'] = details.details
		name = ""
		if details.details_Galaxies_id:
			print("galaxy")
			name = get_galaxy_name(details.id)
		if details.details_Solar_Systems_id:
			print("solar system")
			name = get_Solar_System_name(details.id)
		if details.details_Planets_id:
			print("planet")
			name = get_Planet_name(details.id)
		print(name)
		dic['classname'] = get_classname(name)
		dic['path_of_img'] = "info/pics/" + get_classname(name) + ".jpg"
		All.append(dic)
	return All
