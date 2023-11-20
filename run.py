#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from galaxies import Galaxie
from solar_systems import Solar_System
from planets import Planet
from details import Detail





in_put = ""
comands = {
	"for new galaxy": "new galaxy",
	"for new solar system": "new solar system",
	"for new planet": "new planet",
	"if tyou wanna exit": "Exit"
}

while (in_put != "Exit"):
	in_put = input(srt(comands) + '\n')
	print(in_put)
