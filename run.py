#!/usr/bin/python3
from galaxies import Galaxie
from solar_systems import Solar_System
from planets import Planet
from details import Detail
from functions import new
from functions import all
from functions import count





in_put = ""
comands = {
	"for new galaxy": "new galaxy",
	"for new solar system": "new solar_system",
	"for new planet": "new planet",
	"for display Universe": "all",
	"if tyou wanna exit": "Exit",
	"to know number of galaxies": "count galaxies",
	"to know number of solar systems": "count solar_systems",
	"to know number of planets": "count planets"
}

while (in_put != "Exit"):
	print(comands)
	in_put = input(">>> ")
	list_split = in_put.split()
	if list_split:
		if list_split[0] == "new" and len(list_split) == 2:
			new(list_split[1])
		elif list_split[0] == "all" and len(list_split) == 1:
			all()
		elif list_split[0] == "count" and len(list_split) == 2:
			count(list_split[1])
		elif list_split[0] == "Exit" and len(list_split) == 1:
			pass
		else:
			print("syntax error!!")
