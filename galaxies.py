#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class Galaxie(Base):
	__tablename__ = "Galaxies"
	id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name = Column(String(128), nullable=False)
	solar_Systems = relationship("Solar_System")
	details = relationship("Detail")

	def __init__(self, name):
		self.name = name
