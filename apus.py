# -*- coding: utf-8 -*-
import pandas as pd
from mp import *
import math
import inspect
from common import *

class Apu(object):
	def calc(self, materiales, mo, type):
		self.type = type
		self.materiales = pd.DataFrame(data=materiales, columns=['material','unidad','cantidad','pu', 'tipo'])
		self.materiales['valor'] = self.materiales['cantidad'] * self.materiales['pu']
		self.pu_mat = round(self.materiales['valor'].sum())
		self.valor_mat = round(self.pu_mat * self.cantidad, 0)

		self.mo = pd.DataFrame(data=mo, columns=['tarea','unidad','pu'])
		self.mo['cantidad'] = self.cantidad
		self.mo['valor'] = self.mo['cantidad'] * self.mo['pu']
		self.pu_mo = round(self.mo['pu'].sum())
		self.valor_mo = round(self.pu_mo * self.cantidad, 0)

		self.valor = self.valor_mat + self.valor_mo
		self.r = [self.name, self.type, self.unidad, self.cantidad, self.pu_mat + self.pu_mo, self.valor]
		
		self.mp = res_mp(self.materiales, self.cantidad)
		valor_mp = round(self.mp['valor'].sum(),0)

	def show(self):
		print 
		print("total")
		print(self.r)
		print
		print("apu")
		print(self.materiales)

	def show_mp(self):
		print
		print("mp")
		print(self.mp)
		print("total mp", self.valor_mp)

class Pared(Apu):
	def __init__(self, name, cantidad):
		self.name = name
		self.cantidad = cantidad
		self.unidad = "m2"
		ladrillo = Ladrillo()
		pintura = Pintura()
		materiales = [
			ladrillo.material,
			ladrillo.brecha_horz(grosor=0.02, mezcla=Cemento(160)),
			ladrillo.brecha_vert(grosor=0.02, mezcla=Cemento(160)),
			["pañete interior", "m3", 0.015, Cemento(160).valor, Cemento(160)],
			["pañete exterior", "m3", 0.015, Cemento(160).valor, Cemento(160)],
			["pintura interior", "galon", pintura.consumo_m2, pintura.pu, pintura],
			["pintura exterior", "galon", pintura.consumo_m2, pintura.pu, pintura],
		]

		mo = [
			["pegar bloque", "m2", 10000],
			["pañetar", "m2", 8000],
			["pintar", "m2", 2000],
		]
		self.calc(materiales, mo, 'wall')

		def composicion():
			pass

class Estructura(Apu):
	def __init__(self, name, cantidad, area, num_varillas):
		self.name = name
		self.cantidad = cantidad
		self.unidad = "m"
		lado = math.sqrt(area) - .05
		materiales = [
			["Varilla", "m", num_varillas, Varilla('1/2"').pu, Varilla('1/2"')],
			["Estribo", "m", (4*lado + .1) /.15, Varilla('1/4"').pu, Varilla('1/4"')],
			["Concreto", "m3", area, Cemento(420).valor, Cemento(420)],
			["Tabla", "un", 1, Encofrado('estructura').pu, Encofrado('estructura')],
		]

		mo = [
			["columnas", "m", 16000],   #20000
		]
		self.calc(materiales, mo, 'column')

class Beam(Apu):
	def __init__(self, name, cantidad, area, num_varillas):
		self.name = name
		self.cantidad = cantidad
		self.unidad = "m"
		lado = math.sqrt(area) - .05
		materiales = [
			["Varilla", "m", num_varillas, Varilla('1/2"').pu, Varilla('1/2"')],
			["Estribo", "m", (4*lado + .1) /.15, Varilla('1/4"').pu, Varilla('1/4"')],
			["Concreto", "m3", area, Cemento(420).valor, Cemento(420)],
			["Tabla", "un", 1, Encofrado('estructura').pu, Encofrado('estructura')],
		]

		mo = [
			["vigas", "m", 16000],  #20000
		]
		self.calc(materiales, mo, 'beam')

class Placa(Apu):
	def __init__(self, name, cantidad, espesor):
		self.name = name
		self.cantidad = cantidad
		self.espesor = espesor
		self.unidad = "m2"
		materiales = [
			["Malla", "	m2", 1, Malla().pu, Malla()],
			["Concreto", "m3", espesor, Cemento(420).valor, Cemento(420)],
			["Encofrado", "un", 1, Encofrado('placa').pu, Encofrado('placa')],
		]

		mo = [
			["placa", "m2", 40000],
		]
		self.calc(materiales, mo, 'slab')

class Piso(Apu):
	def __init__(self, name, cantidad):
		self.name = name
		self.cantidad = cantidad
		self.unidad = "m2"
		materiales = [
			["Concreto antepiso", "m3", 0.05, Cemento(300).valor, Cemento(300)], # pedro, 6 pacas/m3 = 300kg de cemento
			["tableta", "m2", 1, Tableta().pu, Tableta()],
			["Cemento pegar", "m3", .01, Cemento(160).valor, Cemento(160)]
			# ["Cemento pegar", "m3", 1, 5000], # pedro, 4 m2 / paca => con espesor 1cm 4 * .01 = .04 m3 => 50kg / .04 = 1250kg de cemento, no es logico
		]

		mo = [
			["antepiso", "m2", 5000],
			["tableta", "m2", 10000],
		]
		self.calc(materiales, mo, 'floor')

class Techo(Apu):
	def __init__(self, name, cantidad):
		self.name = name
		self.cantidad = cantidad
		self.unidad = "m2"
		materiales = [
			# ["teja barro", "m2", 1, Teja().pu, Teja()],
			["teja polip", "m2", 1, Teja_polipropileno().pu, Teja_polipropileno()],
			["machimbre", "m2", 1, Machimbre().pu, Machimbre()],
			["viguetas", "m", 1.25, Viguetas().pu, Viguetas()],  	# cada 80 cm para propileno, 40 cm para teja
		]

		mo = [
			["machimbre", "m2", 15000],
			["maderas", "m2", 15000],
			["acerolit", "m2", 12000],
			# ["teja barro", "m2", 40000],
		]
		self.calc(materiales, mo, 'ceiling')

class Bano(Apu):
	def __init__(self, name, cantidad, area):
		self.name = name
		self.cantidad = cantidad
		self.area = area
		self.unidad = "un"
		materiales = [
			['Sanitario tao single Blanco Corona', 'un', 1,	116000, Tipo('sanitario', 116000)],
			['Lavamanos colgar Happy Bone Corona', 'un', 1, 75000, Tipo('lavamanos', 75000)],
			['Grifería lavamanos sencilla Dalia', 'un', 1, 16400, Tipo('griferia', 16400)],
			['Regadera básica gris 1 función + brazo Stretto', 'un', 1, 35000, Tipo('regadera', 35000)],
			['Piso Caristo Beige 33.8X33.8cm Caja 1.6 m2', 'un', area, 13900, Tipo('piso baño', 13900)],
		]
		
		mo = [
			["enchape 2.5x1.2 + 2", "un", 75000],
			["puntos 3", "un", 54000],
			["punto luz", "un", 30000],
		]
		self.calc(materiales, mo, 'bathroom')

class Puerta(Apu):
	def __init__(self, name, cantidad):
		self.name = name
		self.cantidad = cantidad
		self.unidad = "un"
		pu = 161000
		materiales = [
			['puerta 204x80', 'un', 1,	pu, Tipo('puerta', pu)],
		]
		
		mo = [
			["puertas", "un", 20000],
		]
		self.calc(materiales, mo, 'door')

class PuertaGaraje(Apu):
	def __init__(self, name, cantidad):
		self.name = name
		self.cantidad = cantidad
		self.unidad = "un"
		pu = 600000
		materiales = [
			['puerta 240x240', 'un', 1,	pu, Tipo('puerta garaje', pu)],
		]
		
		mo = [
			["puertas garaje", "un", 20000],
		]
		self.calc(materiales, mo, 'door_garage')

class Ventana(Apu):
	def __init__(self, name, cantidad):
		self.name = name
		self.cantidad = cantidad
		self.unidad = "un"
		pu = 144000
		materiales = [
			['ventana pvc', 'un', 1, pu, Tipo('ventana', pu)],
		]
		
		mo = [
			["ventanas", "un", 20000],
		]
		self.calc(materiales, mo, 'window')

class Cocina(Apu):
	def __init__(self, name, cantidad):
		self.name = name
		self.cantidad = cantidad
		self.unidad = "un"
		pu = 800000
		materiales = [
			['Sanitario tao single Blanco Corona', 'un', 1,	pu, Tipo('cocina', pu)],
		]
		
		mo = [
			["MO", "un", 50000],
			["puntos 2", "un", 36000],
			["punto luz", "un", 30000],
		]
		self.calc(materiales, mo, 'kitchen')