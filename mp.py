# -*- coding: utf-8 -*-
import pandas as pd

class Tipo(object):
	def __init__(self, nombre, pu):
		self.tipo = nombre
		self.unidad = 'un'
		self.cantidad_mp = 1
		self.pu = pu


class Ladrillo(object):
	def __init__(self):
		self.tipo = 'ladrillo'
		self.unidad = 'un'
		self.nombre = 'Ladrillo #4 40x20x9cm 5k 12.5u/m2'
		self.cantidadxm2 = 12.5
		self.pu = 1300
		self.alto = 0.2 
		self.ancho = 0.4 
		self.profundo = 0.09
		self.cantidad_mp = 1
		self.material = ["ladrillo #4", "un", self.cantidadxm2, self.pu, self]
	
	def brecha_horz(self, grosor, mezcla):
		volumen = 1 / self.alto * grosor * self.ancho * self.profundo
		return ["brecha horz",	"m3", volumen, mezcla.valor, mezcla]
	
	def brecha_vert(self, grosor, mezcla):
		volumen = 1 / self.ancho * grosor * self.alto * self.profundo
		return ["brecha vert",	"m3", volumen, mezcla.valor, mezcla]

class Cemento(object):
	def __init__(self, cantidad=1):
		self.tipo = 'cemento'
		self.nombre = 'cemento'
		self.unidad = 'kg'
		self.empaque = 'paca'
		self.contenido = 50
		self.precio = 16500
		self.cantidad_mp = cantidad
		self.pu = self.precio / self.contenido
		self.valor = cantidad * self.pu

	# pedro tiene Cemento antepiso se necesitan 6 pacas/m3 = 300kg de cemento

class Pintura(object):
	def __init__(self):
		self.tipo = 'pintura'
		self.unidad = 'galon'
		self.nombre = "pintura Constructor Pro 200 Sherwim Williams"
		self.unidad_empaque = '4 cuñetes de 5 galones'
		self.precio = 425000
		self.contenido_galones = 4 * 5
		self.rendimiento_m2xgalon = 30
		self.cantidad_mp = 1
		self.pu = self.precio / self.contenido_galones
		self.consumo_m2 = round(1. / self.rendimiento_m2xgalon, 3)

class Varilla(object):
	def __init__(self, diametro):
		self.tipo = 'varilla ' + diametro
		self.unidad = 'm'
		self.cantidad_mp = 1
		self.precio = {
			'12mm': 10700,
			'11mm': 9560,
			'3/8"': 6820,
			'1/2"': 11970,
			'1/4"': 3485,
			'9mm': 6100,
			'8.5mm': 5960
		}
		self.longitud_m = 6
		self.pu = self.precio[diametro] / self.longitud_m

class Encofrado(object):
	def __init__(self, tarea):
		self.tipo = 'encofrado'
		self.unidad = 'm2'
		self.cantidad_mp = 1
		self.precio = {
			'estructura': 2000,
			'placa': 5000,
		}
		self.pu = self.precio[tarea]

class Malla(object):
	def __init__(self):
		self.tipo = 'malla'
		self.unidad = 'm2'
		self.cantidad_mp = 1
		self.nombre = 'Malla 15x15cm espesor 4.0mm 6mx2.35m 18.8kg'
		self.precio = 43000.
		self.largo = 6.
		self.ancho = 2.35
		self.pu = round(self.precio / self.largo / self.ancho, 0)

class Tableta(object):
	def __init__(self):
		self.tipo = 'tableta'
		self.unidad = 'm2'
		self.cantidad_mp = 1
		self.nombre = 'tableta 20cm x 20cm'
		self.precio_m2 = 8000
		self.ancho = .2 
		self.largo = .2
		self.cantidad = 1 / self.ancho * 1 / self.largo
		self.pu = self.precio_m2

class Teja(object):
	def __init__(self):
		self.tipo = 'teja'
		self.unidad = 'm2'
		self.cantidad_mp = 1
		self.nombre = 'Teja española 42 x 21 x 23 cm 2 kilos 18 u/m2	800'
		self.precio_m2 = 14400
		self.un_m2 = 18
		self.pu = self.precio_m2

class Teja_polipropileno(object):
	def __init__(self):
		self.tipo = 'teja'
		self.unidad = 'm2'
		self.cantidad_mp = 1
		self.nombre = 'Teja Roja #8 Trapezoidal 0.94x2.44 metros Polipropileno Koyo'
		self.precio = 22900
		self.un_m2 = 1 / .94 / 2.44
		self.precio_m2 = self.precio * self.un_m2
		self.pu = self.precio_m2

class Machimbre(object):
	def __init__(self):
		self.tipo = 'machimbre'
		self.unidad = 'm2'
		self.cantidad_mp = 1
		self.nombre = 'Machimbre pino 9 mm x 9 cm x 3.2 m'
		self.precio = 7900
		self.ancho = 0.09 
		self.largo = 3.2 
		self.pu = round(self.precio / self.largo / self.ancho, 0)

class Viguetas(object):
	def __init__(self):
		self.tipo = 'viguetas'
		self.unidad = 'm'
		self.cantidad_mp = 1
		self.nombre = 'Pino 2 x 4 pulgadas 3,96 metros dimensionado'
		self.precio = 28900
		self.largo = 3.96 
		self.pu = round(self.precio / self.largo, 0)