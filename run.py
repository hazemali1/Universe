#!/usr/bin/python3
from galaxies import Galaxie
from solar_systems import Solar_System
from planets import Planet
from details import Detail
from functions import new
from functions import all





in_put = ""
comands = {
	"for new galaxy": "new galaxy",
	"for new solar system": "new solar_system",
	"for new planet": "new planet",
	"for display Universe": "all",
	"if tyou wanna exit": "Exit",
	"\n": "\n"
}

while (in_put != "Exit"):
	in_put = input(comands)
	list_split = in_put.split()
	if list_split:
		if list_split[0] == "new":
			new(list_split[1])
		elif list_split[0] == "all":
			all()
		else:
			print("syntax error!!")
	else:
		print("syntax error!!")
