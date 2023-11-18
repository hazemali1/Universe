#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Planets(Base):
	__tablename__ = "Planets"
	id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name = Column(String(128), nullable=False)
	solar_system_id = Column(Integer, ForeignKey("solar_systems_id"), nullable=False)
	details = relationship("detail")

	def __init__(self, name, solar_system_id):
		self.name = name
		self.solar_system_id = solar_system_id
