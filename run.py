#!/usr/bin/python3
from galaxies import Galaxie
from solar_systems import Solar_System
from planets import Planet
from details import Detail
from db import session



obj1 = Galaxie("Galaxie1")
session.add(obj1)
session.commit()

obj2 = Solar_System("Solar_System1", galaxie_id=obj1.id)
session.add(obj2)
session.commit()

obj3 = Planet("Planets1", solar_system_id=obj2.id)
session.add(obj3)
session.commit()

obj4 = Detail("Details for galaxy", details_Galaxies_id=obj1.id)
session.add(obj4)
session.commit()

obj5 = Detail("Details for solar system", details_Solar_Systems_id=obj2.id)
session.add(obj5)
session.commit()

obj6 = Detail("Details for planet", details_Planets_id=obj3.id)
session.add(obj6)
session.commit()
