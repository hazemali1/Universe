#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Solar_System(Base):
	__tablename__ = "Solar_Systems"
	id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name = Column(String(128), nullable=False)
	galaxie_id = Column(Integer, ForeignKey("Galaxies.id"), nullable=False)
	planets = relationship("Planets")
	details = relationship("Details")

	def __init__(self, name, galaxie_id):
		self.name = name
		self.galaxie_id = galaxie_id
