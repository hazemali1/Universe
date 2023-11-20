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

in_put = ""
comands = {
	"for new galaxy": "new galaxy",
	"for new solar system": "new solar system",
	"for new planet": "new planet",
	"if tyou wanna exit": "Exit"
}

while (in_put != "Exit"):
	in_put = input(comands)
	print(in_put)
