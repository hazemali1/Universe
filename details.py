#!/usr/bin/python3
from sqlalchemy import column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Details(Base):
	__tablename__ = "Details"
	details = Column(String(4069), nullable=False)
	details_for_id = column(Integer, ForeignKey("details_for_id"), nullable=False)

	def __init__(self, details, details_for_id):
		self.details = details
		self.details_for_id = details_for_id
