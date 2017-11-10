#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function 
import pandas as pd
from apus import *

class Obra(object):
	def __init__(self, nombre, apus):
		self.nombre = nombre
		self.apus = apus
		self.items = pd.DataFrame(data=[x.r for x in apus], columns=["nombre", "type", "unidad", "cantidad", "pu", "valor"])
		self.valor = self.items['valor'].sum()
		self.valorf = "{:,}".format(self.valor)

		self.res_items = res_apus(apus)
		
		self.mp = [x.mp for x in apus]
		if len(self.mp) > 1:
			self.mp = pd.concat(self.mp)
		else:
			self.mp = pd.DataFrame(data=self.mp[0], columns=["tipo", "unidad", "pu", "cantidad_apu", "cantidad", "valor"])
		self.mp = res(self.mp, 'tipo')
		self.valor_mp = self.mp['valor'].sum().round(0)

		self.mo = res_mo_obra(self.apus)
		self.valor_mo = self.mo['valor'].sum().round(0)

	def show_items(self):
		print("\nitems " + self.nombre)
		print(self.items)
		print("total", self.valorf)

	def show_res_items(self):
		print("\nres items")
		print(self.res_items)
		print("total", "{:,}".format(round(self.res_items['valor'].sum(),0)))

	def show_mp(self):
		print("\nmp " + self.nombre)
		print(self.mp)
		print("total", "{:,}".format(self.valor_mp))

	def show_mo(self):
		print("\nmo " + self.nombre)
		print(self.mo)
		print("total", "{:,}".format(self.valor_mo))

	def show_apus(self):
		print("\nobra", self.nombre)
		print(self.apus)
		print("total", self.valorf)

	def item(self, nombre):
		i = self.items.loc[self.items['nombre']==nombre].index[0]
		return self.apus[i]


class Obras(object):
	def __init__(self, nombre, obras):
		self.nombre = nombre
		self.obras = obras

		self.items = res_items_obras(self.obras)
		self.valor_items = self.items['valor'].sum()

		self.mp = res_mp_obras(self.obras)
		self.valor_mp = self.mp['valor'].sum()

		self.mo = res_mo_obras(self.obras)
		self.valor_mo = self.mo['valor'].sum()

	def show(self):
		print(self.obras)
						
	def show_obras(self):
		for obra in self.obras:
			obra.show_items()
			obra.show_res_items()
			obra.show_mp()
			obra.show_mo()
			print("\nmp+mo", "{:,}".format(obra.valor_mp + obra.valor_mo))

	def show_res_items(self):
		print("\nres items")
		print(self.apusg)
		print("total", "{:,}".format(round(self.apusg['valor'].sum(),0)))

	def show_mp(self):
		print("\nmp " + self.nombre)
		print(self.mp)
		print("total", "{:,}".format(self.valor_mp))

	def show_mo(self):
		print("\nmo " + self.nombre)
		print(self.mo)
		print("total", "{:,}".format(self.valor_mo))