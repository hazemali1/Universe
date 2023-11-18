#!/usr/bin/python3
from galaxies import Galaxie
from solar_systems import Solar_System
from planets import Planet
from details import Detail
from db import db



obj1 = Galaxie("Galaxie1")
db.add(obj1)
db.commit()

obj2 = Solar_System("Solar_System1", galaxie_id=obj1.id)
db.add(obj2)
db.commit()

obj3 = Planet("Planets1", solar_system_id=obj2.id)
db.add(obj3)
db.commit()

obj4 = Detail("Details for galaxy", details_Galaxies_id=obj1.id)
db.add(obj4)
db.commit()

obj5 = Detail("Details for solar system", details_Solar_Systems_id=obj2.id)
db.add(obj5)
db.commit()

obj6 = Detail("Details for planet", details_Planets_id=obj3.id)
db.add(obj6)
db.commit()
