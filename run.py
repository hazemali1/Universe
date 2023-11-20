#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from galaxies import Galaxie
from solar_systems import Solar_System
from planets import Planet
from details import Detail
from functions import new





in_put = ""
comands = {
	"for new galaxy": "new galaxy",
	"for new solar system": "new solar system",
	"for new planet": "new planet",
	"if tyou wanna exit": "Exit"
}

while (in_put != "Exit"):
	in_put = input(comands)
	list_split = in_put.split()
	print(in_put)
	if list_split:
		if list_split[0] == "new":
			new(list_split[1])
