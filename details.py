#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Details(Base):
	__tablename__ = "Details"
	details = Column(String(4069), nullable=False)
	details_Galaxies_id = Column(Integer, ForeignKey("Galaxies.id"))
	details_Solar_Systems_id = Column(Integer, ForeignKey("Solar_Systems.id"))
	details_Planets_id = Column(Integer, ForeignKey("Planets.id"))

	def __init__(self, details, details_for_id):
		self.details = details
		self.details_for_id = details_for_id
