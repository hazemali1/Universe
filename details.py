#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Detail(Base):
	__tablename__ = "Details"
	details = Column(String(4069), nullable=False)
	id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	details_Galaxies_id = Column(Integer, ForeignKey("Galaxies.id"))
	details_Solar_Systems_id = Column(Integer, ForeignKey("Solar_Systems.id"))
	details_Planets_id = Column(Integer, ForeignKey("Planets.id"))

	def __init__(self, details, **kwargs):
		self.details = details
		for k, v in kwargs.items():
			if k == "details_Galaxies_id":
				self.details_Galaxies_id = v
		for k, v in kwargs.items():
			if k == "details_Solar_Systems_id":
				self.details_Solar_Systems_id = v
		for k, v in kwargs.items():
			if k == "details_Planets_id":
				self.details_Planets_id = v
