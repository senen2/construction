# -*- coding: utf-8 -*-
import pandas as pd
from obra import *

sala = Obra('sala', apus=[
		Estructura("columnas 22x22", 2*3.44 + 2*2.78, area=.22*.22, num_varillas=4),
		Estructura("vigas 22x22", 7.7 + 2.82 + 1.2 + 4.1, area=.22*.22, num_varillas=4),
		Estructura("columnas 30x30", 4*2.7, area=.3*.3, num_varillas=8),
		Estructura("vigas 30x30", 5*7.71 + 2*4.78 + 2*6.18, area=.3*.3, num_varillas=10),
		Placa("losa", 4.2*7.7 + 1.2*1.2 + 1.25*1.38, .15),
		Piso("piso", 5.66*7.7),
		Pared("paredes", (1.2 + 1.25 + 4.2 + 7.7 + 4.2 + 1.25 + 4)*2.78 + .9*2.5 + (2.67 + 1.2)*2.88),
		Bano("baños", 1, 2.5*1.2),
		Puerta("puertas", 3),
		Ventana("ventanas", 2),
		Placa("escalera", (4 + 1.2 + 1.48)*1.2, .17),
	]
)

oficina = Obra('oficina', apus=[
		Estructura("columnas 22x22", 6*2.78, area=.22*.22, num_varillas=4),
		Estructura("vigas 22x22", 2*6.18 + 2*7.9, area=.22*.22, num_varillas=4),
		Pared("paredes", (2*5.9 + 2*7.95)*2.78),
		Placa("techo", 8*8.3, .12),
		Piso("piso", 4.2*7.7),
		Ventana("ventanas", 4),
	]
)

garaje = Obra('garaje', apus=[
		Estructura("columnas 22x22", 9*2.78, area=.22*.22, num_varillas=4),
		Estructura("vigas 22x22", 2*6.62 + 2*6.46 + 2*6.18, area=.22*.22, num_varillas=4),
		Pared("muro contencion", 6.67*1.38),
		Pared("paredes", (5.87 + 6.8 - 2*2.4*2)*2.78),
		Placa("techo", 7*7, .12),
		Piso("piso", 5.83*6.8),
		PuertaGaraje("puertas garaje", 2),
	]
)

sep = Obra('pared separacion', apus=[
		Estructura("columnas 22x22", 3*1.98, area=.22*.22, num_varillas=4),
		Estructura("vigas 22x22", 6.9 + 7.12, area=.22*.22, num_varillas=4),
		Pared("paredes", (6.9 - 2*.22)*1.98),
	]
)

hab = Obra('habitaciones', apus=[
		Estructura("columnas 22x22", 15*2.78, area=.22*.22, num_varillas=4),
		Estructura("vigas 22x22", 3*16.8 + 3.9 + 2.4, area=.22*.22, num_varillas=4),
		Piso("piso", 16.6*3.9 +16.6*2.38),
		Pared("paredes", (4*4 + 2*16.6)*2.78),
		Placa("techo", 17*7.8, .12),
		Ventana("ventanas", 4),
		Puerta("puertas", 4),
		Bano("baños", 2, 2.5*1.2),
	]
)

salon = Obra('salon', apus=[
		Estructura("columnas 22x22", 6*2.78 + 2.18, area=.22*.22, num_varillas=4),
		Estructura("vigas 22x22", 6*8.1 + 2*9.8, area=.22*.22, num_varillas=4),
		Pared("muro contencion", 6.67*1.38),
		Pared("paredes", (2*4 + +2.5)*2.78 + 8.1*2.18),
		Placa("techo", 8.2*7.4, .12),
	]
)

todo = Obras('todo', [sala, oficina, garaje])#, sep, salon, hab])
todo.show_obras()
print "\ntotal items", "{:,}".format(todo.valor_items)

print todo.show_mp()
print todo.show_mo()
print "\nmp+mo", "{:,}".format(todo.valor_mp + todo.valor_mo)
